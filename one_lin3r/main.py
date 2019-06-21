# -*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci ( One-Lin3r )
from .core import Cli
from .core.color import *
import argparse

parser = argparse.ArgumentParser(prog='One-Lin3r.py')
parser.add_argument("-r", help="Execute a resource file.")
parser.add_argument("-x", help="Execute a specific command (use ; for multiples).")
parser.add_argument("-q",action="store_true", help="Quiet mode (no banner).")
args    = parser.parse_args()

liners     = Cli.db.index_liners()
def main():
    if not args.q:
        Cli.utils.banner(liners)

    if args.x:
        for c in args.x.split(";"):
            Cli.start(c)
        Cli.start()
    elif args.r:
        try:
            f = open(args.r,"r")
        except:
            error("Can't open the specifed resource file!")
            exit(0)
        cmds = f.readlines()
        for cmd in cmds:
            Cli.start(cmd.strip())
        Cli.start()
    else:
        Cli.start()
    #You think it's simple when you look here huh :"D
    sys.exit()

#if __name__ == '__main__':
#    main()
