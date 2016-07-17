import re,os,shutil
regex=re.compile(r'''^(.*?)
	((0|1)?\d)-
	((0|1)?\d)-
	((19|20)\d\d)
	(.*?)$''',re.VERBOSE)

for filename in os.listdir():
	mo=regex.search(filename)
	if mo==None:
		continue
	before=mo.group(1)
	month=mo.group(2)
	day=mo.group(4)
	year=mo.group(6)
	after=mo.group(8)
	newName=before+day+'-'+month+'-'+year+after
	abspath=os.path.abspath('.')
	filename=os.path.join(abspath,filename)
	newName=os.path.join(abspath,newName)
	print('Renaming %s to %s '%(filename,newName))

	shutil.move(filename,newName)

