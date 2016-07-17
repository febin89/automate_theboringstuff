import traceback
try:
	raise Exception('This i sthe error')
except:
	filen=open('errorlog','w')
	filen.write(traceback.format_exc())
	filen.close()
	print('The traceback info was mwritten')
