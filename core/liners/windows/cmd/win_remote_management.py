class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Windows Remote Management provides the ability to remotely execute wmi commands."
    function    = "Execute"
    liner       = 'winrm qc -q & winrm i c wmicimv2/Win32_Process @{CommandLine="COMMAND"}'
