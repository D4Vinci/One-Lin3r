class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Search for 'password' string in file contents using find"
    function    = "PrivEsc"
    liner       = 'find . -type f -exec grep -i -I "PASSWORD" {{}} /dev/null \;'
