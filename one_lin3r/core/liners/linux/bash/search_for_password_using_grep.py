class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Search for 'password' string in file contents using grep"
    function    = "PrivEsc"
    liner       = '''grep --color=auto -rnw '/' -ie "PASSWORD" --color=always 2> /dev/null'''
