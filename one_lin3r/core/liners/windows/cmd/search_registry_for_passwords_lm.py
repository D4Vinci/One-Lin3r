class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Search registry local machine tree for 'password' string"
    function    = "PrivEsc"
    liner       = 'REG QUERY HKLM /F "password" /t REG_SZ /S /K'
