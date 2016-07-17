#!python3
#mcb.py-Saves and loads pieces of text to the clipboard
import shelve,pyperclip,sys

shelf=shelve.open('mcb')

if len(sys.argv)==3 and sys.argv[1].lower()=='save':
	shelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
	if sys.argv[1].lower()=='list':
		pyperclip.copy(str(list(shelf.keys())))
	elif sys.argv[1] in shelf:
		pyperclip.copy(shelf[sys.argv[1]])



shelf.close()
