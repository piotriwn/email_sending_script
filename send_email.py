# prerequisites:
# 1. Turn on "Less secure app access"
# 2. Go to https://accounts.google.com/DisplayUnlockCaptcha

# SMPT Gmail ports
# https://support.google.com/mail/answer/7126229?hl=en
# SSL: 465
# TLS/STARTTLS: 587


import smtplib, ssl
import getpass
# these handle Multipurpose Internet Mail Extensions
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SSL_PORT = 465
MY_EMAIL = "piotrDevTest@gmail.com"

def send_email(password, text=None, htmlText = "HTML Email body", subject="Hello world", sender = MY_EMAIL, sendTo=None):
    # make sure sendTo is an instance of list type
    # if not, it raises Assertion Error
    assert isinstance(sendTo, list), "Send-to paramater is not a list"

    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = ", ".join(sendTo) # CSV formatted recipient list
    message["Subject"] = subject

    plainTextPart = MIMEText(text, 'plain')
    htmlTextPart = MIMEText(htmlText, 'html')

    # # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(plainTextPart)
    message.attach(htmlTextPart)

    messageString = message.as_string()

    context = ssl.create_default_context() # Create a secure SSL context

    with smtplib.SMTP_SSL(host = "smtp.gmail.com", port = SSL_PORT, context = context) as server:
        server.login(MY_EMAIL, password)
        server.sendmail(sender, sendTo, messageString)


password = getpass.getpass(prompt = "Enter password: ", stream=None)
text = input("Type message body: ")
htmlText = text
subject = input("Type subject: ")

send_email(password = password, text = text, htmlText = htmlText, subject = subject, sendTo= ["piotrek.iwn+testDevEmail@gmail.com"])