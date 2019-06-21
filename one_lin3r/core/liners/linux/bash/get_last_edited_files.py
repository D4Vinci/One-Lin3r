class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Get files that were edited in the last 10 minutes"
    function    = "PrivEsc"
    liner       = 'find / -mmin -10 2>/dev/null | grep -Ev "^/proc"'
