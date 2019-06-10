class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Get IIS Web config"
    function    = "PrivEsc"
    liner       = 'Get-Childitem –Path C:\inetpub\ -Include web.config -File -Recurse -ErrorAction SilentlyContinue'
