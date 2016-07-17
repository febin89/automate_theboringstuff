import time,subprocess
timeLeft=8
while timeLeft>0:
	print(timeLeft)
	time.sleep(1)
	timeLeft-=1

subprocess.Popen(['see','l.mp3'])

