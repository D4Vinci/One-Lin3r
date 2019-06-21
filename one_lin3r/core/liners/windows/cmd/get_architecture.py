class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Extracts windows architecture with wmic"
    function    = "PrivEsc"
    liner       = 'wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%'
