#!python3
#backuptoZip.py-This program creates the versions of backup everytime it is zipped
import os,zipfile

def backuptozip(folder):

#	folder=os.path.abspath(folder)


	number=1
	while True:
		zipfilename=os.path.basename(folder)+'_'+str(number)+'.zip'
		if not os.path.exists(zipfilename):
			break
		number=number+1
	print('Creating the zip file %s..'%(zipfilename))
	backupzip=zipfile.ZipFile(zipfilename,'w')
	for foldername,subfolders,filenames in os.walk(folder):
		print('Adding files in %s..'%(foldername))
		backupzip.write(foldername)
		for filename in filenames:
			newbase=os.path.basename(folder)+'_'
			if filename.startswith(newbase) and filename.endswith('.zip'):
				continue
			backupzip.write(os.path.join(foldername,filename))
	backupzip.close()
			
	print('Done')
backuptozip('../shell')
