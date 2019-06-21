class info:
    author      = "Karim shoair (D4Vinci)"
    description = "List all crob jobs for all users in the system (Needs root ofc)"
    function    = "PrivEsc"
    liner       = 'for user in $(cut -f1 -d: /etc/passwd); do echo $user; crontab -u $user -l; done'
