import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.outlook.com', 587)
server.ehlo()
server.starttls()
server.login('BotSender1204@outlook.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'Idan Bronfman'
msg['To'] = 'idan.brbr@outlook.com'
msg['Subject'] = 'Just A TEST'

with open('message.txt','r') as f:#normal read
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'image.jpg'
attachment = open(filename,'rb')#read bytes because it is an image and not a text

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('BotSender1204@outlook.com','idan.brbr@outlook.com',text)

server.quit()