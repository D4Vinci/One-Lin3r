class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Using wmic to search for unquoted services paths so you can exploit it later"
    function    = "PrivEsc"
    liner       = '''wmic service get name,displayname,pathname,startmode |findstr /i "Auto" |findstr /i /v "C:\Windows\\" |findstr /i /v """'''
