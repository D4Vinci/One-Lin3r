class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Disable firewall using netsh"
    function    = "PrivEsc"
    liner       = 'netsh firewall set opmode disable & netsh advfirewall set allprofiles state off'
