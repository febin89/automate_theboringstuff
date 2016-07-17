import os

for folder,subfolders,filename in os.walk('/home/febi/lin-class/python'):
	print('The current folder is '+folder)
	for subfolder in subfolders:
		print('SubFolder of '+folder+':'+subfolder)
	for filen in filename:
		print('FIle inside ' +folder+':'+filen)
	print(' ')
