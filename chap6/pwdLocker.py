#!python3
#An insecure password locker program
passwords={'email':'AAde321',
	   'blog':'asdQW21',
	   'luggage':'21212'}
import sys
if len(sys.argv)<2:
	print('Usage:python pwdLocker.py [account]-copy account password')
	sys.exit()
account=sys.argv[1]
if account in passwords:
	
	print('Password for '+account+' copied to the clipboard')
else:
	print('There is no account namrs '+account)	 

