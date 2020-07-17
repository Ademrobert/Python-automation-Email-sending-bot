import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='the email what will be sending all the emails '
to_addr=['place the people who you want to send emails here', 'like this']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='made by Adem Follow him on Github'

body='Follow adem on Github'

msg.attach(MIMEText(body,'plain'))

email='the email what will be sending all the emails'
password='the emails password what will be sending all the emails'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()