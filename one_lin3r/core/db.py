#Written by: Karim shoair - D4Vinci ( One-Lin3r )
import os
try:
    import importlib
except:
    import imp as importlib
from . import utils

def index_liners():
    # Return list of all liners
    # TODO: change liners path
    liners = []
    pth      = utils.get_corefilepath("liners", "")
    for path,_, files in os.walk( pth ):
        for name in [f for f in files if f.endswith(".py")]:
            liners.append( os.path.join(path, name) )
    liners = [ x for x in liners if ("__" not in x and x.endswith('.py')) ]
    liners = utils.my_map( lambda x:x.replace(pth,""),liners)
    liners = utils.my_map( lambda x:x.replace(".py","").replace("\\","/"), liners)
    return liners

def grab(liner):
    liner_exec  = importlib.import_module( ".core.liners."+utils.pythonize(liner), package='one_lin3r' )
    importlib.reload(liner_exec)
    return getattr(liner_exec, 'info')
