import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "socializepots@gmail.com"
email_password = os.environ.get("EMAIL_PASSWORD")

subject = "You have been invited to a pot!"
body = """
You have been invited to a pot! Click the link below to join the pot!
"""

def sendInvites(peersArray):
    for peer in peersArray:
        if peer != "":
            print("Sending email to " + peer)
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = email_sender
            msg['To'] = peer
            msg.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, peer, msg.as_string())

