# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( One-Lin3r )
from .Core import Cli
from .Core.color import *
import argparse

parser = argparse.ArgumentParser(prog='One-Lin3r.py')
parser.add_argument("-r", help="Execute a resource file (history file).")
parser.add_argument("-x", help="Execute a specific command (use ; for multiples).")
parser.add_argument("-q",action="store_true", help="Quit mode (no banner).")
args    = parser.parse_args()

def main():
    if not args.q:
        Cli.banner()

    if args.x:
        for c in args.x.split(";"):
            Cli.start(c)
    elif args.r:
        try:
            f = open(args.r,"r")
        except:
            error("Can't open the specifed history file!")
            exit(0)
        cmds = f.readlines()
        for cmd in cmds:
            Cli.start(cmd.strip())
    else:
        Cli.start()
    #You think it's simple when you look here huh :"D
    sys.exit()
