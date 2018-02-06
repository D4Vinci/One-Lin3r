# One-Lin3r [![n0where best cybersecurity tools](https://img.shields.io/badge/6-This%20year%20top%20100%20tools-red.svg)](https://n0where.net/best-cybersecurity-tools) [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Core](https://img.shields.io/badge/Core-1.0-red.svg) ![Database](https://img.shields.io/badge/Database-0.4-red.svg)

One-Lin3r is simple and light-weight framework inspired by the web-delivery module in Metasploit.

[![asciicast](https://asciinema.org/a/157020.png)](https://asciinema.org/a/157020?autoplay=1)

It consists of various one-liners that aids in penetration testing operations:
- **Reverser**: Give it IP & port and it returns a reverse shell liner ready for copy & paste.
- **Dropper**: Give it an uploaded-backdoor URL and it returns a download-&-execute liner ready for copy & paste.
- **Other**: Holds liners with general purpose to help in penetration testing (ex: Mimikatz, Powerup, etc...) on the trending OSes (Windows, Linux, and macOS) "More OSes can be added too".

## Features
- Search for any one-liner in the database by its full name or partially.
- You can add your own liners by [following these steps](https://github.com/D4Vinci/One-Lin3r/wiki) to create a ".liner" file.Also you can send it to me directly and it will be added in the framework and credited with your name :smile:.
- Autocomplete any framework command and recommendations in case of typos (in case you love hacking like movies :laughing:).
- Command line arguments can be used to give the framework a resource file to load and execute for automation.
- The ability to reload the database if you added any liner without restarting the framework.
- You can add any platform to the payloads database just by making a folder in payloads folder and creating a ".liner" file there.
- More...

The payloads database is not big now because this the first edition but it will get bigger with updates and contributions.

# Screenshots
<img src="https://github.com/D4Vinci/One-Lin3r/blob/master/Core/resources/oneliner1.png" width="50%"></img><img src="https://github.com/D4Vinci/One-Lin3r/blob/master/Core/resources/oneliner2.png" width="50%"></img>
<img src="https://github.com/D4Vinci/One-Lin3r/blob/master/Core/resources/oneliner3.png" width="50%"></img><img src="https://github.com/D4Vinci/One-Lin3r/blob/master/Core/resources/oneliner4.png" width="50%"></img>


# Usage

## Commandline arguments
```
usage: One-Lin3r.py [-h] [-r R] [-x X] [-q]

optional arguments:
  -h, --help  show this help message and exit
  -r          Execute a resource file (history file).
  -x          Execute a specific command (use ; for multiples).
  -q          Quit mode (no banner).
```

## Framework commands
```
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
exit/quit           Exit the framework
`````

## Installing and requirements
### To make the tool work at its best you must have :
- Python 3.x or 2.x (preferred 3).
- Linux (Tested on kali rolling) or Windows system (Not tested yet on MacOS but it should work).
- The requirements mentioned in the next few lines.

### Installing
**+For windows : (After downloading ZIP and upzip it)**
```
cd One-Lin3r-master
python -m pip install -r win_requirements.txt
python One-Lin3r.py -h
```
**+For Linux :**
```
git clone https://github.com/D4Vinci/One-Lin3r.git
chmod 777 -R One-Lin3r
cd One-Lin3r
pip install -r requirements.txt
python One-Lin3r.py -h
```

## Contact
- [Twitter](https://twitter.com/D4Vinci1)

## Donation
If you liked my work and want to support me, you can give me a cup of coffee :)

<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/donate.png"></img>

bitcoin address: 1f4KfYikfqHQzEAsAGxjq46GdrBKc8jrG

## Disclaimer
One-Lin3r is created to help in penetration testing and it's not responsible for any misuse or illegal purposes.

Copying a code from this tool or using it in another tool is accepted as you mention where you get it from :smile:.

> Pull requests are always welcomed :D
