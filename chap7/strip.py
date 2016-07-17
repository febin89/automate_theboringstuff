import sys,re
txt=sys.argv[1]
regex=re.compile(r'[\s]*')
#print(sys.argv[0] + sys.argv[1]+' ' +sys.argv[2])
if len(sys.argv)<2:
	mo=regex.search(sys.argv[1])

	if mo!=None:
		print(mo.group())
else:
	reg=re.compile('^'+sys.argv[2]+'|'+sys.argv[2] +'$')
	mo=reg.sub('',sys.argv[1])
	print(mo)
	#if mo!=None:
		#print(mo.group())
