# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
def sendEmail(message):
    from_email = Email("daninotific@gmail.com")
    to_email = To("daniahmedkhatri@gmail.com")
    subject = "Dollar Rate"
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)