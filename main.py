# ikhxwsrvaubogeti
from email.message import EmailMessage
import ssl
import smtplib

email_list = ['aarthi.bansode@gmail.com', 'saikumari.bansode@gmail.com', 'contact.rahulbm@gmail.com', 'harun.bansode@gmail.com']

email_sender = 'contact.harunbansode@gmail.com'
email_password = 'ikhxwsrvaubogeti'
email_receiver = 'neyoloh544@dronetz.com'
subject = 'This is my First Email Through Python.'

body = """
        Hello Everyone,
        
        This is my first email sending through python...
        
        Regards,
        Harun Bansode
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print('Email sent....')