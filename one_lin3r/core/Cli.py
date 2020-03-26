# -*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci ( One-Lin3r )
import os, sys, time, re, argparse
from terminaltables import SingleTable as table
import importlib,traceback,pyperclip
from . import utils,db
from .color import *

liners     = db.index_liners()
all_keywords = ["banner","refresh","reload","search","list","show","use","info","history","makerc",
				"exit","quit","?","help","set","copy","variables","resource","os"]
variables = {
	"TARGET":'',
	"PORT":'',
	"URL":'',
	"COMMAND":'',
	"FILE_PATH":'',
	"USERNAME":'',
	"PASSWORD":''
}

name = W+underline+"OneLiner"+end
history = []
debug = False

# To use with search command
Search_parser = argparse.ArgumentParser(prog="search",add_help=False)
Search_parser.add_argument('keywords', nargs='*', default="", help='Search database for a specific liner by its name, author name or function.')
Search_parser.add_argument('-h', action="store_true", help="Show this help message.") # I done that because print the normal help exits the framework
Search_parser.add_argument('-f', action="store_true", help='Performs a full search in all liners information.')
Search_parser.add_argument('-d', action="store_true", help='Performs a deep search like full search but with liners.')
Search_parser.add_argument('-l', action="store_true", help='Search in liners only without including any info.')
Search_parser.add_argument('-a', action="store_true", help='Search for liners that matches any keyword included.')

def start(rc=False):
	help_msg = """
	Command                     Description
	--------                    -------------
	help/?                      Show this help menu.
	list/show                   List all one-liners in the database.
	search  (-h) [Keywords..]   Search database for a specific liner by its name, author name or function.
	use         <liner>         Use an available one-liner.
	copy        <liner>         Use an available one-liner and copy it to clipboard automatically.
	info        <liner>         Get information about an available liner.
	set <variable> <value>      Sets a context-specific variable to a value to use while using one-liners.
	variables                   Prints all previously specified variables.
	banner                      Display banner.
	reload/refresh              Reload the liners database.
	check                       Prints the core version and checks if you are up-to-date.
	history                     Display command-line most important history from the beginning.
	makerc                      Save command-line history to a file.
	resource     <file>         Run the commands stored in a file
	os          <command>       Execute a system command without closing the framework
	exit/quit                   Exit the framework"""

	#if os.name!="nt":
	#	utils.Input_completer(all_keywords)

	while True:
		try:
			if rc:
				cmd = rc
				print("\n"+name+G+" > "+end+cmd)
			else:
				cmd = utils.getinput_autocompleted("\n"+name+G+" > "+end, all_keywords, variables.keys(), liners)

			cmd = cmd.strip()
			for c in cmd.split(';'):
				if c=="" or c[0]=="#":continue
				if len( cmd.split(";") ) > 1:
					print(G+" > "+end+ c)
				head = c.lower().split()[0]
				args = " ".join(c.split()[1:])

				if head in ["banner","history","makerc","quit","exit","?","help"]:
					if head=="banner":
						utils.banner(liners)

					if head=="history":
						n = -1
						for i in range( len(history) ):
							print( history[n] )
							n -= 1

					if head=="makerc":
						file_name = "history.txt"
						if args and len(args.split())>0:
							file_name = args.split()[0]
						f = open(file_name,"w")
						for line in history:
							f.write(line+"\n")
						f.close()
						status( "Command history saved to "+file_name )

					if head in ["help","?"]:
						print(help_msg)

					if head in ["exit","quit"]:
						exit(0)
				else:
					command_handler(c)
		except KeyboardInterrupt:
			print("")
			error("KeyboardInterrupt use exit command!")
			continue
		finally:
			if rc:
				time.sleep(0.1)
				break

#A function for every command (helpful in the future)
def command_handler(c):
	#parsing a command and pass to its function
	command = c.lower().split()[0]
	args    = " ".join(c.split()[1:])
	try:
		handler = globals()["command_{}".format(command)]
		handler(args)
		history.append(c)
	except Exception as e:
		if command not in all_keywords:
			error( command + " is not recognized as an internal command !")
			#To check for the wanted command on typos
			wanted = utils.grab_wanted(command,all_keywords)
			if len(wanted)>0:
				status( "Maybe you meant : " + wanted )
		else:
			error( "Error in executing command "+ command )
			if debug:
				print(e)
				traceback.print_exc()
		status( "Type help or ? to learn more..")

def command_search(text=False):
	try:
		cmd = Search_parser.parse_args(text.split())
	except:
		cmd = Search_parser.parse_args("") # Fuck you argparse, next time I will use more flexible module like getopt globally
		# I done this because any error argparse gives is printed and it exit the framework but now no

	if cmd.h or not cmd.keywords:
		# error("You must enter a keyword to search for !")
		print(Search_parser.format_help(), end="")
		return

	else:
		cols = [end+W+"#", end+B+Bold+"Name", end+B+Bold+"Function"+end]
		Columns = []
		text = [i.lower() for i in cmd.keywords]
		n = 1
		for p in liners:
			if cmd.d:
				info = db.grab(p)
				full_text = " ".join([p, info.author, info.description, info.function, info.liner]).lower()
			elif cmd.f:
				info = db.grab(p)
				full_text = " ".join([p, info.author, info.description, info.function]).lower()
			elif cmd.l:
				info = db.grab(p)
				full_text = info.liner.lower()
			else:
				info = db.grab(p)
				full_text = " ".join([p, info.author, info.function]).lower()

			if len(text)==1 and text[0] in full_text:
				Columns.append([end+W+str(n).ljust(3," "), end+G+p+end ,function_colorize(info.function)])
				n+=1
			elif len(text)>1:
				result = []
				for word in text:
					if word in full_text:
						result.append(True)
					else:
						if not cmd.a:
							result.append(False)
							break
						else:
							pass
				if all(result) or (" ".join(text) in full_text):
					Columns.append([end+W+str(n).ljust(3," "), end+G+p+end ,function_colorize(info.function)])
					n+=1
		if not Columns:
			error("Didn't find a liner matches the entered keywords!")
		else:
			utils.create_table(cols,Columns)

def command_list(text=False):
	cols = [end+W+"#", end+B+Bold+"Name", end+B+Bold+"Function"+end]
	Columns = []
	text = text.lower()
	n = 1
	for p in liners:
		info = db.grab(p)
		Columns.append([end+W+str(n).ljust(3," "), end+G+p+end ,function_colorize(info.function)])
		n+=1
	utils.create_table(cols,Columns)

def command_show(text=False):
	command_list(text)

def command_set(text=False):
	if not text or len(text.split())<2:
		error("Command syntax is incorrect!")
	else:
		option, value = text.split()[:2]
		global variables
		variables[option.upper()] = value
		status("Variable %(option)s set to %(value)s"%locals()) # Yeah, looks awesome when using locals :D

def command_variables(text=False):
	if len(variables.keys())==0:
		error("No variables set yet!")
	else:
		cols = [end+W+"#", end+B+Bold+"Name", end+B+Bold+"Value"+end]
		Columns = []
		n = 1
		for key, value in variables.items():
			if not variables[key]:
				Columns.append([end+W+str(n), end+G+key+end, R+"None"+end])
			else:
				Columns.append([end+W+str(n), end+G+key+end, M+value+end])
			n+=1
		utils.create_table(cols,Columns)

def command_use(p=False,auto=False):
	if not p:
		error("You must enter a liner to use !")
		if auto:
			return False
	else:
		p = p.lower()
		if p.lower() in liners:
			info = db.grab(p)
			liner = info.liner
			for variable in variables.keys():
				if variables[variable]:
					liner = liner.replace(variable.upper(),variables[variable])
			status(B+"Your liner is: "+end+M+liner)
			if auto:
				return liner
			# Modern problems requires modern solutions :D
		else:
			error(p+" liner doesn't exist !")
			if auto:
				return False

def command_copy(p=False):
	ok = command_use(p,True)
	if ok:
		pyperclip.copy(ok)
		status("Liner copied to clipboard successfully!")

def command_info(p=False):
	if not p:
		error("You must enter a liner to get its information !")
	else:
		liner   = p.lower()
		if liner in liners:
			info = db.grab(liner)
			all_variables = []
			for variable in variables.keys():
				if variable.upper() in info.liner:
					all_variables.append(variable)
			status( B+"Liner added by "+G+"=> "+M+info.author+end )
			status( B+"Function       "+G+"=> "+M+function_colorize(info.function)+end )
			status( B+"Variables used "+G+"=> "+(M+(B+", "+end+M).join(all_variables) if all_variables else R+"None")+end )
			status( B+"Description    "+G+"=> "+M+info.description+end )
		else:
			error(p+" liner doesn't exist !")

def command_reload(text=False):
	global liners
	liners = db.index_liners()
	status("Database updated! ( {} liners loaded )".format( len(liners) ) )

def command_refresh(text=False):
	command_reload(text)

def command_check(text=False):
	status("Checking...")
	with open(utils.get_corefilepath("resources","version.txt")) as f:
		v = f.read().strip()
	status("Core version: "+Y+v+end)
	lol = utils.check_version()
	if lol and lol==v:
		status("You are up-to-date!")
	elif not lol:
		error("Error in connection! Check your internet!")
	else:
		#TODO: Auto update
		error("The latest core database is "+lol)
		status("Consider updating the framework ASAP for new features and liners!")

def command_resource(p=False):
	try:
		with open(p,"r") as f:
			cmds = f.readlines()
			for cmd in cmds:
				start(cmd.strip())
	except:
		if not p:
			error("Enter a resource file to read!")
		else:
			if debug:
				print("    Input -> "+str(p))
				print("      Dir -> "+str(os.getcwd()))
			error("Can't open the specifed resource file!")
		return

def command_os(text=False):
	if text:
		os.system(text)
	else:
		error("You must enter a command to execute !")
		return

def command_debug(text=False):
	global debug
	debug = (debug!=True)
	status("Debug mode is turned "+{True:"On",False:"Off"}[debug])
