edappallyjn={'ns':'green','ew':'red'}
lulujn={'ns':'red','ew':'green'}

def switchLights(stopLight):
	for key in stopLight.keys():
		if stopLight[key]=='red':
			stopLight[key]=='green'
		elif stopLight[key]=='green':
			stopLight[key]='yellow'
		elif stopLight[key]=='yellow':
			stopLight[key]='red'
	assert 'red' in stopLight.values(),'Neither light is red! '+str(stopLight)
switchLights(lulujn)
