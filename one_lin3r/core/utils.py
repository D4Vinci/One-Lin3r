#Written by: Karim shoair - D4Vinci ( One-Lin3r )
from __future__ import print_function,unicode_literals
from terminaltables import AsciiTable as table
from .color import *
from prompt_toolkit.shortcuts import CompleteStyle, prompt
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import sys, os, time, pkg_resources

try:
	from urllib.request import urlopen
except ImportError:
	from urllib import urlopen

core_dir = pkg_resources.resource_filename('one_lin3r', 'core')

def get_corefilepath(*args):
	return os.path.join(core_dir, *args)

current_directory = os.getcwd()

def banner(liners):
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")
	banner  = open(get_corefilepath("resources", "banner.txt")).read()
	v = open(get_corefilepath("resources", "version.txt")).read().strip()
	banner_to_print  = R
	banner_to_print += banner.format(Name=G+"One-Lin3r By "+Bold+"D4Vinci -"+M+" V"+v+end+R,
									  Description=B+"A framework where all your liners belongs to..."+R,
									   Loaded=G+"Loaded "+Y+str(len(liners))+G+" liner(s)."+R)
	print(banner_to_print+end)
	return

def my_map(func,values):
	# Because map behaves differently in python 2 and 3, I decided to write my own fuckin version :3
	result = []
	for value in values:
		result.append( func(value) )
	return result

not_allowed_chars= ['\\','[','>','$','<','#','"','%',';','*','?','/','!','.','+','^','&','=','-',']','|','(',')','@','}','~','`',':',',','{',"'"]
def my_filter(values, forbidden=not_allowed_chars):
	values = list(set(values))
	returned = []
	for element in values:
		result_boolens = []
		for char in forbidden:
			if char in element:
				result_boolens.append(False)
			else:
				result_boolens.append(True)
		if all(result_boolens):
			returned.append(element)
	return returned

def grab_wanted(cmd,keywords):
	#To check for the wanted command on typos
	wanted = ""
	for i in reversed(range(1,5)): # Danger! Magic,don't touch :"D
		oo = [s for s in keywords if (s[:i]==cmd[:i] and s not in wanted) ]
		if len(oo)>1:
			wanted += ", ".join(oo)
		elif len(oo)==1:
			wanted += ", "+oo[0]
	return wanted

def pythonize(path):
	# Normal path to python importable path
	return path.lower().replace('/', '.').replace("\\",".")

def humanize(path):
	# Python importable path to normal path
	return path.lower().replace('.', '/')

def create_table(headers,rows,name="liners"):
	# Prints a table with the given parameters
	# print(table([["Header1","Header2"],["Row"]],"name").table)
	Main = [headers]
	for row in rows:
		Main.append(row)
	t = table(Main,name)
	t.inner_column_border = True
	t.outer_border	= False
	t.inner_heading_row_border = True
	t.inner_footing_row_border = False
	print("\n"+t.table)

def encoder(text):
	import base64
	ver = sys.version[0]
	if ver=="3":
		return base64.b64encode(text.encode()).decode()
	else:
		return base64.b64encode(text.encode())

def check_version():
	#check for database version online
	u = "https://raw.githubusercontent.com/D4Vinci/One-Lin3r/master/one_lin3r/core/resources/version.txt"
	try:
		res = urlopen(u).read().decode('utf-8').strip()
		return res
	except:
		return None

# Welcome to my own custom auto completer ( Don't touch it's art :D )
# If you gonna borrow/steal it, be nice and mention the source ;)
class MyCompleter(Completer):
	def __init__(self, commands, variables, liners):
		self.commands  = sorted([c.lower() for c in commands])
		self.variables = sorted([v.lower() for v in variables])
		self.liners    = sorted([l.lower() for l in liners])
	def get_completions(self, document, complete_event):
		buffer = document.text.lower()
		line = document.text.lower().split()
		# show all commands
		if not line:
			for i in self.commands:
				yield Completion(i, start_position=-1 * len(document.text), display=i)
		else:
			cmd = line[0].strip()
			if cmd in self.commands:
				if buffer.startswith("use") or buffer.startswith("info"):
					if len(line)>1: # if any part of a liner is after the command
						result = []
						# Search for liners starts with the part typed
						for l in self.liners:
							if l.startswith(line[1]):
								result.append(l)
						# If no liners found, search for liners that contains the word typed ;)
						# Example: `use iis` (tab) would become `use windows/powershell/get_iis_config`
						if len(result)==0:
							for l in self.liners:
								if line[1] in l:
									result.append(l)

						# All liners should start with command typed because the line would be overwritten
						if len(result):
							for i in range(len(result)):
								if buffer.startswith("use"):
									result[i] = "use "+result[i]
								else:
									result[i] = "info "+result[i]
						for l in result:
							yield Completion(l, -document.cursor_position, display=l)
					else: # If no liner typed, return all liners
						for l in self.liners:
							yield Completion(l, -document.cursor_position, display=l)

				elif buffer.startswith("set"):
					# No need for comments, it's the same logic as the above...
					if len(line)>1:
						result = []
						for v in self.variables:
							if v.startswith(line[1]):
								result.append("set "+v)
						if len(result)==0:
							result = [v for v in self.variables if line[1] in v]

						for v in result:
							yield Completion(v, -document.cursor_position, display=v)
					else:
						for v in self.variables:
							yield Completion(v, -document.cursor_position, display=v)
			else:
				result = []
				for c in self.commands:
					if c.startswith(cmd):
						result.append(c)
				if len(result)==0:
					for i in reversed(range(1,5)): # Fixing typos to return matches if there's no matches :D
						result.extend( [ c for c in self.commands if (c[:i]==cmd[:i] and c not in result) ])
						if len(result)>0:
							result = sorted(result)
							break

				for c in result:
					yield Completion(c, start_position=-document.cursor_position, display=c)


session = PromptSession(history=FileHistory(os.path.expanduser("~/.command_history")))
def getinput_autocompleted(name, commands, variables, liners):
	text = session.prompt( ANSI(name),
							completer=MyCompleter(commands, variables, liners),
							complete_while_typing=True,
							complete_in_thread=True,
							complete_style=CompleteStyle.READLINE_LIKE
						)
	return text
