#Written by: Karim shoair - D4Vinci ( One-Lin3r )
import sys,os,time
from terminaltables import SingleTable as table
try:
	from urllib.request import urlopen
except ImportError:
	from urllib import urlopen

def getinput():
	# Return the suitable input type according to python version
	try:
		return raw_input
	except NameError:
		return input

def create_table(headers,rows,name="Payloads"):
	# Prints a table with the given parameters
	# Was having borders consisting of non-ascii chars but removed it now this better :3
	#print(table([["Header1","Header2"],["Row"]],"name").table)
	Main = []
	Main.append(headers)
	for row in rows:Main.append(row)
	t = table(Main,name)
	#Added this before releasing the tool and too lazy to remove all the things about the table title :"D
	t.inner_column_border = False
	t.outer_border	= False
	t.inner_heading_row_border = False
	t.inner_footing_row_border = False
	#Ok removed it xD
	print("\n"+t.table)

def url_verifier(url=""):
	# Use Django url verifier regex to check
	import re
	regex = re.compile(
		r'^(?:http|ftp)s?://' # http:// or https://
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		r'localhost|' #localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		r'(?::\d+)?' # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	try:
		regex.search(url).group()
		return True
	except:
		return False

def encoder(text):
	import base64
	ver = sys.version[0]
	if ver=="3":
		return base64.b64encode(text.encode()).decode()
	else:
		return base64.b64encode(text.encode())

def check_ver(ver):
	#check for database version online
	u = "https://raw.githubusercontent.com/D4Vinci/One-Lin3r/master/Core/"
	if ver==0:
		v = open(os.path.join("Core","resources","version.txt")).read().strip()
		u = u + 'resources/version.txt'
	else:
		v = open(os.path.join("Core","payloads","version.txt")).read().strip()
		u = u + 'payloads/version.txt'
	try:
		res = urlopen(u).read().decode('utf-8').strip()
	except:
		return 2
	if v==res:
		return 0
	else:
		return res
	#Will work on this function in future to make it update the database but not now

"""
def slow_print(text):
	for s in text:
		if sys.version_info[0]==2:
			sys.stdout.write(s)
		else:
			print(s, end='')
	time.sleep(0.1)
"""

class MyCompleter(object):
	def __init__(self, options):
		self.options = sorted(options)
	def complete(self, text, state):
		if state == 0: # build possible matches
			if text:
				self.matches = [s for s in self.options if s and s.startswith(text)]
			else:  # all possible matches
				self.matches = self.options[:]
		try:
			return self.matches[state]
		except IndexError:
			return None

def Input_completer(keywords):
	if os.name!="nt":
		import readline
		completer = MyCompleter(keywords)
		readline.set_completer(completer.complete)
		readline.parse_and_bind('tab: complete')

#Will add in the feature a function to autocomplete liners
