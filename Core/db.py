#Written by: Karim shoair - D4Vinci ( One-Lin3r )
import os

def index_payloads():
    # Return list of all payloads
    payloads = []
    pth      = os.path.join("Core","payloads")
    for path,_, files in os.walk( pth ):
        for name in [f for f in files if f.endswith(".liner")]:
            payloads.append( os.path.join(path, name) )
    return payloads

def grab(payload,wanted="info"):
    # Return data from payload
    try:
        import ConfigParser as configparser
    except:
        import configparser
    config = configparser.ConfigParser()
    config.read(payload)
    if wanted !="info":
        data = {
    "Type":config.get("Payload","Type"),
    "Payload":config.get("Payload","Payload")
    }
    else:
        data = {
    "Author":config.get("Info","Author"),
    "Payload type":config.get("Payload","Type"),
    "Description":config.get("Info","Description")
    }
    return data
