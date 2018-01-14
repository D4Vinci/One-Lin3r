# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( One-Lin3r )
import os,sys
global G, Y, B, R, W , M , C , end ,Bold,underline
def set_colors():
	global G, Y, B, R, W , M , C , end ,Bold,underline
	if os.name=="nt":
		try:
			import win_unicode_console , colorama
			win_unicode_console.enable()
			colorama.init()
			#green - yellow - blue - red - white - magenta - cyan - reset
			G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
			Bold = "\033[1m"
			underline = "\033[4m"
		except:
			G = Y = B = R = W = G = Y = B = R = Bold = underline = ''
	else:
		#import colorama
		#colorama.init()
		#green - yellow - blue - red - white - magenta - cyan - reset
		G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
		Bold = "\033[1m"
		underline = "\033[4m"

set_colors()

def status(text):
	print( C+"[+] "+G+text+end )

def error(text):
	print( M+"[!] "+R+text+end )

def warning(text):
	print( B+"[!W!] "+Y+text+end )

def goodbye():
	print(G+" Thanks for playing with "+B+"One-Lin3r! "+R+"<3"+end)
	exit(0)
