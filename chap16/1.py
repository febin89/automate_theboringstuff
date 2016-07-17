import smtplib
obj=smtplib.SMTP('www.yahoo.com',465)
obj.ehlo()
obj.starttls()
obj.login('feb18989@yahoo.com','1891989')
obj.sendmail('feb18989@yahoo.com','feb18989@gmail.com','Sub:SO long.\nGood to see you')
obj.quit()
