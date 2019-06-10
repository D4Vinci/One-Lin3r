class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses forfiles to execute commands without using cmd."
    function    = "Execute"
    liner     = """forfiles /p c:\windows\system32 /m notepad.exe /c COMMAND"""
