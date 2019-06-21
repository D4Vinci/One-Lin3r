class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Quering wmi to search for unquoted services paths so you can exploit it later"
    function    = "PrivEsc"
    liner       = '''gwmi -class Win32_Service -Property Name, DisplayName, PathName, StartMode | Where {$_.StartMode -eq "Auto" -and $_.PathName -notlike "C:\Windows*" -and $_.PathName -notlike '"*'} | select PathName,DisplayName,Name'''
