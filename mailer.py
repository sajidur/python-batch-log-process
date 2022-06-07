import smtplib

class Mailer:
     def __init__(self, name, age):
        self.name = name
        self.age = age

     def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
        """this is some test documentation in the function"""
        message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        # Send the mail
        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, message)
        server.quit()