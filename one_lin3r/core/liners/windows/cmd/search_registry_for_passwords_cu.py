class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Search registry current user tree for 'password' string"
    function    = "PrivEsc"
    liner       = 'REG QUERY HKCU /F "password" /t REG_SZ /S /K'
