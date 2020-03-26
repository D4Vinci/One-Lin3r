# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( One-Lin3r )
import os,sys

#green - yellow - blue - red - white - magenta - cyan - reset
G, Y, B, R, W, M, C, end, Bold, underline = '\033[32m', '\033[93m', '\033[94m', '\033[31m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m', "\033[1m", "\033[4m"
if os.name=="nt":
	try:
		import win_unicode_console , colorama
		# win_unicode_console.enable()  # Removed due to some unicode confilct on some windows devices
		colorama.init()
	except:
		G = Y = B = R = W = M = C = end = Bold = underline = ''

#Colors available: green - yellow - blue - red - white - magenta - cyan - reset
colored_functions = {
	"reverse shell":end+M+"Reverse Shell"+end,
	"bind shell":end+B+"Bind Shell"+end,
	"Dropper":end+R+"Dropper"+end,
	"Loader":end+Y+"Loader"+end,
	"Nmap script":end+W+"Nmap script"+end,
	"PrivEsc":end+C+"PrivEsc"+end,
	"Execute":end+G+"Execute"+end
}

def function_colorize(text):
	for key,value in colored_functions.items():
		if key.lower() in text.lower():
			text = text.lower().replace(key.lower(),value)
	return text

def status(text):
	print( C+"[+] "+G+text+end )

def error(text):
	print( M+"[!] "+R+text+end )
