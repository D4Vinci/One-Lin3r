class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Query the local machine AlwaysInstallElevated from the registry to check if msi files are always installed elevated."
    function    = "PrivEsc"
    liner       = 'reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated'
