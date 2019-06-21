class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Querying wmi from powershell to get all running processes."
    function    = "PrivEsc"
    liner       = 'Get-WmiObject -Query "Select * from Win32_Process" | where {$_.Name -notlike "svchost*"} | Select Name, Handle, @{Label="Owner";Expression={$_.GetOwner().User}}} | ft -AutoSize'
