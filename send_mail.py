from mail_server import MailServer
from mail_server import SendMail

to_send = "message.txt"
attachment_file = "git.png"

to = 'zigz3883@gmail.com,zz5525492@gmail.com'

userdata = {"zigz5638@gmail.com":""} #enter password here. Gmail > Manage Accounts > App Password > Generate
zigz = SendMail('smtp.gmail.com',465,to_send)
zigz.send_email('zigz5638@gmail.com',to,userdata)
