class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Grabs windows name and version from systeminfo "
    function    = "PrivEsc"
    liner       = 'systeminfo | findstr /B /C:"OS Name" /C:"OS Version"'
