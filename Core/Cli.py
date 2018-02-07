# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( One-Lin3r )
import os,sys,time
from terminaltables import SingleTable as table
from . import utils,db
from .color import *
if os.name!="nt":
	import readline
else:
    import pyreadline

global payloads,all_keywords,name
payloads = db.index_payloads()
all_keywords = ["banner","refresh","reload","search","list","show","use","info","history","save_history","exit","quit","?","help","check"]
name = W+underline+"OneLiner"+end

def start(rc=False):
	myinput = utils.getinput()
	history = []
	help_msg = """
	Command             Description
	--------            -------------
	help/?              Show this help menu
	list/show           List payloads you can use in the attack.
	search  <Keyword>   Search payloads for a specific one
	use     <payload>   Use an available payload
	info    <payload>   Get information about an available payload
	banner              Display banner
	reload/refresh      Reload the payloads database
	check               Prints the core version and database version then check for them online.
	history             Display command line most important history from the beginning
	save_history        Save command line history to a file
	exit/quit           Exit the framework"""
	#back             	Move back from the current context (No we are not in Metasploit :"D )
	if os.name!="nt":
		utils.Input_completer(all_keywords)
	#utils.Payload_completer(payloads)
	while True:
		try:
			if rc:
				c = rc
				print("\n"+name+G+" > "+end+c)
			else:
				c = myinput("\n"+name+G+" > "+end)
			c_head = c.lower().split(" ")[0]
			c_body = " ".join(c.lower().split(" ")[1:])
			if c_head in ["refresh","reload","search","list","show","use","info","exit"]:
				history.append(c)

			if c_head in ["banner","history","save_history","quit","exit","?","help"]:
				if c_head=="banner":
					banner()

				if c_head=="history":
					n = -1
					for i in range( len(history) ):
						print( history[n] )
						n -= 1

				if c_head=="save_history":
					f = open("lin3r_history.txt","w")
					for line in history:
						f.write(line+"\n")
					f.close()
					status( "Command history saved to lin3r_history.txt" )

				if c_head in ["help","?"]:
					print(help_msg)

				if c_head in ["exit","quit"]:
					goodbye()
			else:
				command_handler(c)
		except KeyboardInterrupt:
			print("")
			error("KeyboardInterrupt use exit command!")
			continue
		finally:
			if rc:
				time.sleep(0.3)
				break

#A function for every command (helpful in the future)
def command_handler(c):
	#parsing a command and pass to its function
	command = c.lower().split(" ")[0]
	args    = " ".join(c.lower().split(" ")[1:])
	try:
		handler = globals()["command_{}".format(command)]
		handler(args)
	except:
		error( command + " is not recognized as an internal command !")
		#To check for the wanted command on typos
		wanted = []
		for k in all_keywords:
			if k[:1] == command[:1] or k[:2] == command[:2] or k[:3] == command[:3] or k[:4] == command[:4] :
				wanted.append(k)

		if wanted != []:
			all_w = ""
			for w in wanted:
				all_w += w + "\t"
			status( "Maybe you meant : " + all_w )

		status( "Type help or ? to learn more..")

def command_search(text=False):
	if not text:
		error("You must enter a keyword to search !")
		return
	cols = [B+Bold+"Name"+end,B+Bold+"Payload type"+end,B+Bold+"Description"+end]
	pth = os.path.join("Core","payloads","")
	Columns = []
	Do  = 0;Loaded = 0;
	for p in payloads:
		if text.lower() in p.lower():
			Do = 1
			Loaded+=1
			data = db.grab(p)
			p = p.replace(pth,"").replace(".liner","")
			Des = data["Description"]
			#No,no description shorting any more
			#n    = len(Des)
			#Des_shorted = Des[:int(n/2)]+"-\n"+Des[int(n/2):] if n>60 else Des
			Columns.append([p , data["Payload type"],Des])
	if Do==1:
		utils.create_table(cols,Columns)#,B+Bold+"Payloads Found ( "+str(Loaded)+" Loaded of "+str(len(payloads))+" )"+end)
	else:
		error(text+" Not found!")

def command_list(text=False):
	cols = [G+Bold+"Name"+end,G+Bold+"Payload type"+end,G+Bold+"Description"+end]
	pth = os.path.join("Core","payloads","")
	Columns = []
	for p in payloads:
		data = db.grab(p)
		p    = p.replace(pth,"").replace(".liner","")
		Des  = data["Description"]
		#No,no description shorting any more again
		#n    = len(Des)
		#Des_shorted = Des[:int(n/2)]+"-\n"+Des[int(n/2):] if n>60 else Des
		Columns.append([p , data["Payload type"],Des])
		#Columns.append(["","",""])
	utils.create_table(cols,Columns)#,Bold+"Payloads ( "+str(len(payloads))+" Loaded )"+end)

def command_show(text=False):
	command_list(text)

def command_use(p=False):
	if not p:
		error("You must enter a payload to use !")
		return
	p   = p.lower()
	if os.path.join("Core","payloads",p)+".liner" in payloads:
		myinput = utils.getinput()
		old_p = p
		p = os.path.join("Core","payloads",p)+".liner"
		Author = db.grab(p)["Author"]
		data = db.grab(p,"shit")
		p = p.split(os.sep)[-1].replace(".liner","")
		print( C+"[+] "+B+"This liner added by "+M+Author+end )
		status("Loading payload "+old_p+"...")
		input_line = name+" Payload("+R+p+end+W+")[{}] "+G+"> "+end

		if data["Type"]:
			n=2
			if data["Type"]=="Reverser":n=0
			elif data["Type"]=="Dropper":n=1
			payload = data["Payload"]

		while True: #Any shit to back to this point when the user mistakes :D
			if n==2:#Any other one payload or one line
				print(C+"\n+Final payload "+R+"-> "+payload+end)
				return
				#Added this part of code here because I just added it before releasing

			parameter = myinput(input_line.format({1:"Direct url of the file",0:"IP & port as (ip:port)"}[n]) )
			if n==1:#Dropper case
				if utils.url_verifier(parameter):
					print(C+"\n+Final payload "+R+"-> "+payload.format(parameter)+end)
					return
				else:
					error("Please enter a valid url!")
					continue

			else: #Reverser case
				try:
					ip   = parameter.split(":")[0]
					port = parameter.split(":")[1]
				except:
					error("Write IP && port as ip:port (ex:192.168.1.5:4444)")
					continue
				else:
					print(C+"\n+Final payload -> "+R+payload.format(ip=ip,port=port)+end)
					return
	else:
		error(p+" payload not found!")

def command_list(text=False):
	cols = [G+Bold+"Name"+end,G+Bold+"Payload type"+end,G+Bold+"Description"+end]
	pth = os.path.join("Core","payloads","")
	Columns = []
	for p in payloads:
		data = db.grab(p)
		p    = p.replace(pth,"").replace(".liner","")
		Des  = data["Description"]
		#No,no description shorting any more again
		#n    = len(Des)
		#Des_shorted = Des[:int(n/2)]+"-\n"+Des[int(n/2):] if n>60 else Des
		Columns.append([p , data["Payload type"],Des])
		#Columns.append(["","",""])
	utils.create_table(cols,Columns)#,Bold+"Payloads ( "+str(len(payloads))+" Loaded )"+end)

def command_show(text=False):
	command_list(text)

def command_info(p=False):
	if not p:
		error("You must enter a payload to get it's information !")
		return
	p   = p.lower()
	if os.path.join("Core","payloads",p)+".liner" in payloads:
		old_p = p
		p = os.path.join("Core","payloads",p)+".liner"
		print( C+"[+] "+B+"Payload added by "+G+"=> "+M+db.grab(p)["Author"]+end )
		print( C+"[+] "+B+"Payload type "+G+"=> "+M+db.grab(p)["Payload type"]+end )
		print( C+"[+] "+B+"Description "+G+"=> "+M+db.grab(p)["Description"]+end )
	else:
		error(p+" payload not found!")


def command_reload(text=False):
	global payloads
	payloads = db.index_payloads()
	status("Database updated! ( {} payloads loaded )".format( len(payloads) ) )

def command_refresh(text=False):
	command_reload(text)

def command_check(text=False):
	status("Checking...")
	v1 = open(os.path.join("Core","resources","version.txt")).read().strip()
	v2 = open(os.path.join("Core","payloads","version.txt")).read().strip()
	status("Core version "+Y+v1+G+" Database version "+Y+v2)
	lol = utils.check_ver
	if lol(0)==2 or lol(1)==2:
		error("Couldn't check for the version online!")
		return
	else:
		o1,o2=lol(0),lol(1)
	if (o1==0) and (o2==0):
		status("You are up-to-date!")
	else:
		if o1!=0:
			error("The latest core version is "+o1)
		elif o2!=0:
			error("The latest database version is "+o2)
		else:
			error("The latest core version is "+o1)
			error("The latest database version is "+o2)

def banner():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")
	banner  = open(os.path.join("Core","resources","banner.txt")).read()
	v = open(os.path.join("Core","resources","version.txt")).read().strip()
	banner_to_print  = R
	banner_to_print += banner.format(Name=G+"One-Lin3r By "+Bold+"D4Vinci -"+M+" V"+v+end+R,
									  Description=B+"The one line you always searched for :)"+R,
									   Loaded=G+"Loaded "+Y+str(len(payloads))+G+" payloads."+R)
	print(banner_to_print+end)
	return
