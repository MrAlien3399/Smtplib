from mail_server import MailServer
from mail_server import SendMail

text_message = "message.txt"
attachment_file = "git.png,superman.jpg"

to = 'zigz3883@gmail.com,zz5525492@gmail.com'

userdata = {"zigz5638@gmail.com":""} #enter password here. Gmail > Manage Accounts > App Password > Generate > Mail = Winows App
zigz = SendMail('smtp.gmail.com',465,text_message,attachment_file)
zigz.send_email('zigz5638@gmail.com',to,userdata)
