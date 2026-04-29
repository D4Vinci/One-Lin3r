"""One-Lin3r entrypoint for CLI and MCP server modes.

Examples:
    uv run -m one_lin3r.main
    uv run -m one_lin3r.main -x "list;search reverse shell"
    uv run -m one_lin3r.main --mcp --mcp-transport streamable-http --mcp-port 8000
"""

from __future__ import annotations

import argparse
import io
import inspect
import sys
from contextlib import redirect_stderr, redirect_stdout
from functools import lru_cache

from one_lin3r.core import Cli
from one_lin3r.core.color import error

try:
    from mcp.server.fastmcp import FastMCP
except Exception:  # pragma: no cover - handled via CLI error path
    FastMCP = None


def build_parser() -> argparse.ArgumentParser:
    """Build and return the top-level argument parser."""
    parser = argparse.ArgumentParser(prog="one-lin3r")
    parser.add_argument("-r", help="Execute commands from a resource file.")
    parser.add_argument("-x", help="Execute specific command(s); use ';' for multiple.")
    parser.add_argument("-q", action="store_true", help="Quiet mode (no banner).")
    parser.add_argument("--mcp", action="store_true", help="Start One-Lin3r as an MCP server.")
    parser.add_argument(
        "--mcp-transport",
        default="stdio",
        choices=["stdio", "sse", "streamable-http"],
        help="MCP transport to use (default: stdio).",
    )
    parser.add_argument("--mcp-name", default="One-Lin3r", help="MCP server name.")
    parser.add_argument("--mcp-host", default="127.0.0.1", help="Host for HTTP MCP transports.")
    parser.add_argument("--mcp-port", type=int, default=8000, help="Port for HTTP MCP transports.")
    parser.add_argument(
        "--mcp-path",
        default="/mcp",
        help="Path for streamable-http transport (default: /mcp).",
    )
    return parser


def run_cli(args: argparse.Namespace) -> None:
    """Run One-Lin3r in interactive CLI mode."""
    liners = Cli.db.index_liners()
    if not args.q:
        Cli.utils.banner(liners)

    if args.x:
        for command in args.x.split(";"):
            command = command.strip()
            if command:
                Cli.start(command)
        Cli.start()
        return

    if args.r:
        try:
            with open(args.r, "r", encoding="utf-8") as resource_file:
                commands = resource_file.readlines()
        except OSError:
            error("Can't open the specified resource file!")
            sys.exit(1)

        for command in commands:
            command = command.strip()
            if command:
                Cli.start(command)
        Cli.start()
        return

    Cli.start()


@lru_cache(maxsize=1)
def _cached_liners() -> tuple[str, ...]:
    """Cache liner index to speed up repeated MCP calls."""
    return tuple(Cli.db.index_liners())


def _normalize_liner_name(liner: str) -> str:
    return liner.strip().lower()


def _render_liner_with_variables(liner_name: str) -> str:
    info = Cli.db.grab(liner_name)
    rendered = info.liner
    for variable, value in Cli.variables.items():
        if value:
            rendered = rendered.replace(variable.upper(), value)
    return rendered


def _cli_help_text() -> str:
    """Canonical CLI help text shared with MCP tools."""
    return """
Command                     Description
--------                    -------------
help/?                      Show this help menu.
list/show                   List all one-liners in the database.
search  (-h) [Keywords..]   Search database for a specific liner by its name, author name or function.
use         <liner>         Use an available one-liner.
copy        <liner>         Use an available one-liner and copy it to clipboard automatically.
info        <liner>         Get information about an available liner.
set <variable> <value>      Sets a context-specific variable to a value to use while using one-liners.
variables                   Prints all previously specified variables.
banner                      Display banner.
reload/refresh              Reload the liners database.
check                       Prints the core version and checks if you are up-to-date.
history                     Display command-line most important history from the beginning.
makerc                      Save command-line history to a file.
resource     <file>         Run the commands stored in a file.
os          <command>       Execute a system command without closing the framework.
exit/quit                   Exit the framework.
""".strip()


def build_mcp_server(args: argparse.Namespace) -> FastMCP:
    """Create and configure a FastMCP server instance."""
    init_sig = inspect.signature(FastMCP.__init__)
    init_kwargs = {"json_response": True}
    if "host" in init_sig.parameters:
        init_kwargs["host"] = args.mcp_host
    if "port" in init_sig.parameters:
        init_kwargs["port"] = args.mcp_port
    if "streamable_http_path" in init_sig.parameters:
        init_kwargs["streamable_http_path"] = args.mcp_path
    mcp = FastMCP(args.mcp_name, **init_kwargs)

    @mcp.tool()
    def execute_command(command: str) -> str:
        """Execute one One-Lin3r command and return console output."""
        buffer = io.StringIO()
        with redirect_stdout(buffer), redirect_stderr(buffer):
            Cli.command_handler(command.strip())
        output = buffer.getvalue().strip()
        return output or "Command executed."

    @mcp.tool()
    def list_commands() -> list[dict[str, str]]:
        """List all supported CLI commands with concise descriptions."""
        return [
            {"command": "help/?", "description": "Show help menu."},
            {"command": "list/show", "description": "List all one-liners."},
            {"command": "search", "description": "Search one-liners by keyword(s)."},
            {"command": "use", "description": "Render an available one-liner."},
            {"command": "copy", "description": "Render and copy one-liner to clipboard."},
            {"command": "info", "description": "Show metadata for one-liner."},
            {"command": "set", "description": "Set runtime variable value."},
            {"command": "variables", "description": "List currently set variables."},
            {"command": "banner", "description": "Print One-Lin3r banner."},
            {"command": "reload/refresh", "description": "Reload liner database."},
            {"command": "check", "description": "Check local vs latest core version."},
            {"command": "history", "description": "Show command history."},
            {"command": "makerc", "description": "Save history to file."},
            {"command": "resource", "description": "Execute commands from resource file."},
            {"command": "os", "description": "Execute OS command."},
            {"command": "exit/quit", "description": "Exit CLI."},
        ]

    @mcp.tool()
    def get_help(command: str = "") -> dict[str, str]:
        """Get CLI help text, optionally scoped to a specific command."""
        full_help = _cli_help_text()
        if not command.strip():
            return {"command": "all", "help": full_help}

        normalized = command.strip().lower()
        commands = {entry["command"]: entry["description"] for entry in list_commands()}
        for key, desc in commands.items():
            aliases = [part.strip().lower() for part in key.split("/")]
            if normalized in aliases or normalized == key.lower():
                return {"command": key, "help": f"{key}: {desc}"}

        return {
            "command": normalized,
            "help": "No specific help found for this command. Use list_commands() or get_help() with no args.",
        }

    @mcp.tool()
    def list_liners(platform: str = "", function: str = "") -> list[str]:
        """List available one-liner names, optionally filtered by platform/function."""
        names = list(_cached_liners())
        if platform:
            platform = platform.strip().lower()
            names = [name for name in names if name.startswith(f"{platform}/")]
        if function:
            needle = function.strip().lower()
            names = [name for name in names if needle in Cli.db.grab(name).function.lower()]
        return names

    @mcp.tool()
    def search_liners(
        query: str,
        full: bool = False,
        deep: bool = False,
        liners_only: bool = False,
        any_keyword: bool = True,
        limit: int = 25,
    ) -> list[dict[str, str]]:
        """Search liners by keywords with behavior similar to CLI search flags."""
        keywords = [k.strip().lower() for k in query.split() if k.strip()]
        if not keywords:
            return []

        matches = []
        for name in _cached_liners():
            info = Cli.db.grab(name)
            if deep:
                searchable = " ".join([name, info.author, info.description, info.function, info.liner]).lower()
            elif full:
                searchable = " ".join([name, info.author, info.description, info.function]).lower()
            elif liners_only:
                searchable = info.liner.lower()
            else:
                searchable = " ".join([name, info.author, info.function]).lower()

            if any_keyword:
                ok = any(k in searchable for k in keywords) or (" ".join(keywords) in searchable)
            else:
                ok = all(k in searchable for k in keywords) or (" ".join(keywords) in searchable)
            if ok:
                matches.append(
                    {
                        "name": name,
                        "function": info.function,
                        "author": info.author,
                        "description": info.description,
                    }
                )
            if len(matches) >= max(1, limit):
                break
        return matches

    @mcp.tool()
    def liner_info(liner: str) -> dict[str, str]:
        """Return metadata for a specific one-liner."""
        liner_name = _normalize_liner_name(liner)
        info = Cli.db.grab(liner_name)
        return {
            "name": liner_name,
            "author": info.author,
            "function": info.function,
            "description": info.description,
            "liner": info.liner,
        }

    @mcp.tool()
    def use_liner(liner: str) -> dict[str, str]:
        """Render a liner with current variable values applied."""
        liner_name = _normalize_liner_name(liner)
        info = Cli.db.grab(liner_name)
        return {
            "name": liner_name,
            "function": info.function,
            "rendered": _render_liner_with_variables(liner_name),
        }

    @mcp.tool()
    def list_categories(platform: str = "") -> list[str]:
        """List available top-level platforms or categories within a platform."""
        names = list(_cached_liners())
        if not platform:
            return sorted({name.split("/", 1)[0] for name in names})
        prefix = platform.strip().lower() + "/"
        scoped = [name for name in names if name.startswith(prefix)]
        return sorted({name[len(prefix) :].split("/", 1)[0] for name in scoped if "/" in name[len(prefix) :]})

    @mcp.tool()
    def set_variable(name: str, value: str) -> dict[str, str]:
        """Set a CLI runtime variable used while rendering liners."""
        key = name.strip().upper()
        Cli.variables[key] = value
        return {key: value}

    @mcp.tool()
    def set_variables(values: dict[str, str]) -> dict[str, str]:
        """Set multiple variables in one call."""
        updated = {}
        for key, value in values.items():
            normalized = key.strip().upper()
            Cli.variables[normalized] = value
            updated[normalized] = value
        return updated

    @mcp.tool()
    def clear_variable(name: str) -> dict[str, str]:
        """Clear one variable value."""
        key = name.strip().upper()
        if key in Cli.variables:
            Cli.variables[key] = ""
        return {key: Cli.variables.get(key, "")}

    @mcp.tool()
    def clear_variables() -> dict[str, str]:
        """Clear all variable values."""
        for key in list(Cli.variables.keys()):
            Cli.variables[key] = ""
        return Cli.variables.copy()

    @mcp.tool()
    def refresh_database() -> dict[str, int]:
        """Reload liners database from disk."""
        Cli.command_reload()
        _cached_liners.cache_clear()
        return {"liners": len(_cached_liners())}

    @mcp.resource("oneliner://variables")
    def get_variables() -> dict[str, str]:
        """Get currently configured One-Lin3r variables."""
        return Cli.variables.copy()

    @mcp.resource("oneliner://liners")
    def get_liners_resource() -> list[str]:
        """Get all liner names as a resource."""
        return list(_cached_liners())

    @mcp.prompt()
    def suggest_liner(task: str) -> str:
        """Prompt template for selecting an appropriate one-liner."""
        return (
            "Use the One-Lin3r MCP tools to find a suitable one-liner.\n"
            f"Task: {task}\n"
            "First call list_liners, then inspect likely candidates with liner_info."
        )

    return mcp


def run_mcp(args: argparse.Namespace) -> None:
    """Run One-Lin3r as an MCP server using the selected transport."""
    if FastMCP is None:
        error('MCP SDK not installed. Install with: pip install "mcp[cli]"')
        sys.exit(1)

    mcp = build_mcp_server(args)
    run_sig = inspect.signature(mcp.run)
    run_kwargs = {"transport": args.mcp_transport}
    # Older/newer MCP versions differ here; only pass supported args.
    if args.mcp_transport == "sse" and "mount_path" in run_sig.parameters:
        run_kwargs["mount_path"] = args.mcp_path
    mcp.run(**run_kwargs)


def main() -> None:
    """Parse command line arguments and start CLI or MCP mode."""
    parser = build_parser()
    args = parser.parse_args()
    if args.mcp:
        run_mcp(args)
    else:
        run_cli(args)


if __name__ == "__main__":
    main()
