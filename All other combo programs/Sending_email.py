# app password for gmail: fbnmokklkwldvlag

import smtplib
import getpass

#create smtp object
smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()

smtp_object.starttls()

#to login to google account
email = getpass.getpass('Enter your email:')
password = getpass.getpass('Enter the app password for gamil:')
smtp_object.login(email,password)

#to send the email
sender_email = email
receiver_email = input('enter receiver email:')
subject = input('enter the subject line:')
body = input('enter the message body:')
msg_text = "Subject: "+subject+'\n'+body #in this format request will sent
smtp_object.sendmail(sender_email,receiver_email,msg_text)