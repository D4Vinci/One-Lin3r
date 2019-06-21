class info:
    author      = "Karim shoair (D4Vinci)"
    description = "List all Scheduled tasks using schtasks"
    function    = "PrivEsc"
    liner       = 'schtasks /query /fo LIST 2>nul | findstr TaskName'
