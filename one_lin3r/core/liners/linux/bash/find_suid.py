class info:
    author      = "Nick Aliferopoulos (naliferopoulos)"
    description = "Detects files with SUID bit set, starting from '/' (useful for privilege escalation)"
    function    = "PrivEsc"
    liner       = "find / -perm 4000 2>/dev/null"
