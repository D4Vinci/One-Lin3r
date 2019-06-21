class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Check with nmap scipt for MS17-010 (Eternal Blue) vulnerability."
    function    = "Nmap script"
    liner       = "nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17–010 TARGET"
