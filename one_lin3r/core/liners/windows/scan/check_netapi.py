class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Check with nmap scipt for MS08-067 (NetAPI) vulnerability."
    function    = "Nmap script"
    liner       = "nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms08-067 TARGET"
