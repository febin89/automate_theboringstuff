#!python3

import sys,webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
if len(sys.argv)>2:
	browser=webdriver.Firefox()
	browser.get('https://mail.yahoo.com')
	email=browser.find_element_by_id('login-username')
	email.send_keys('feb18989')
	email=browser.find_element_by_id('login-signin')
	email.click()
	passwd=browser.find_element_by_id('login-passwd')
	passwd.send_keys('1891989')
	passwd.submit()

	text=sys.argv[1]
	address=sys.argv[2]
	compose=browser.find_element_by_id('Compose')
	compose.click()
	compose.send_keys(address)
	compose.send_keys(Keys.TAB)
	compose.send_keys('Test')
	compose.send_keys(Keys.TAB)
	compose.send_keys(text)
	compose.submit()
else:
	print('Wrong usage')

