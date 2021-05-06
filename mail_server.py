import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailServer:
    
    def __init__(self,server,port):
        self.server = server
        self.port = port
    
    def connect_to_smtp_server(self,userdata):
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(self.server,self.port,context=context)
        for user , passwd in userdata.items():
            server.login(user,passwd)
        return server

class SendMail(MailServer):

    def __init__(self,server,port,text_msg=None,attachment=None):
        MailServer.__init__(self,server,port)
        self.text_msg = text_msg
        self.attachment = attachment

    def email_container(self,toaddr):
        
        message = MIMEMultipart()
        message["Subject"] = "Github Project"
        message["From"] = "zigz5638@gmail.com"
        message["To"] = toaddr
        
        if self.text_msg:
            
            with open(self.text_msg,'r') as file:
                text_message = file.read()
                t1 = MIMEText(text_message,"plain")
                message.attach(t1)
        else:
            print("No message provided-Only attachment")
            print("------------------------------------ \n")
        
        
        for attach in self.attachment.split(','):
            
            if attach:
            
                with open(attach,'rb') as file:
                    part = MIMEBase('application','octet-stream')
                    part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={attach}"
                    )
                    message.attach(part)
            else:
                print("No attachment Provided-Only Mail letter")
                print("------------------------------------\n")
        
        return message

    def send_email(self,fromaddr,toaddr,userdata):
        try:
            for to in toaddr.split(','):
                ready2Send = SendMail.email_container(self,to).as_string()
                print(f"Sending to {to}")
                SendMail.connect_to_smtp_server(self,userdata).sendmail(fromaddr,to,ready2Send)
                print(f"Successfully sent to {to} \n")
        except:
            print("Something went wrong!!!")
        finally:
            SendMail.connect_to_smtp_server(self,userdata).quit()

        
