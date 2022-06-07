import smtplib, ssl
import json

class Mailer:
     def __init__(self):
        with open('config.json', 'r') as f:
         config = json.load(f)
         self.smtp_server=config["smtp_server"]
         self.port=config["port"]
         self.sender_email=config["sender_email"]
         self.password=config["password"]


     def send(self,TO,TEXT):
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP(self.smtp_server,self.port)
            server.starttls(context=context) # Secure the connection
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, TO, TEXT)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 