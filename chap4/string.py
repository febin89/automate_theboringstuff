def printPicnic(itemsDict,lWidth,rWidth):
	print('PICNIC ITEMS'.center(lWidth+rWidth,'-'))
	for k,v in itemsDict.items():
		print(k.ljust(lWidth,'.')+str(v).rjust(rWidth))
picnicItems={'sndwiches':4,'apple':12,'cups':4,'cookies':3000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
