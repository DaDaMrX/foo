from smtplib import SMTP
from email.message import EmailMessage


sender_name = 'Python'
sender_addr = '1120151811@bit.edu.cn'
password = '199707161239xX'

receiver_name = 'DaDa'
receiver_addr = 'dadamrxx@gmail.com'

subject = 'Subject'
content = 'Hello'

msg = EmailMessage()
msg['From'] = sender_name + '<' + sender_addr + '>'
msg['To'] = receiver_name + '<' + receiver_addr + '>'
msg['Subject'] = subject
msg.set_content(content)

with SMTP("mail.bit.edu.cn") as smtp:
    smtp.login(sender_addr, password)
    smtp.send_message(msg)
