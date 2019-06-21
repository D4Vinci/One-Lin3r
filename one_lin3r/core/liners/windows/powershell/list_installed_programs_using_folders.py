class info:
    author      = "Karim shoair (D4Vinci)"
    description = "List all installed programs depending on program files folders"
    function    = "PrivEsc"
    liner       = "Get-ChildItem 'C:\Program Files', 'C:\Program Files (x86)' | ft Parent,Name,LastWriteTime"
