#!python3
#mapIt.py-Launches a map in the browser using an address from the commandline                                                                         
import webbrowser,sys,pyperclip
if len(sys.argv)>1:
	address=' '.join(sys.argv[1:])
else:
	address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
