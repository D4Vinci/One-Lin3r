class info:
    author      = "Karim shoair (D4Vinci)"
    description = "List all Scheduled tasks"
    function    = "PrivEsc"
    liner       = 'Get-ScheduledTask | where {$_.TaskPath -notlike "\Microsoft*"} | ft TaskName,TaskPath,State'
