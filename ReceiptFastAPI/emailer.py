from email.message import EmailMessage
import ssl
import smtplib


def email_sender(email_receiver, subject, body):
    email_sender = 'recipiegenie@gmail.com'
    email_password = 'jifc bcwi tkzr prvf'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())
        server.quit()
