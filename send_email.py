import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "charlieedoherty@gmail.com"
    print("\n\n\n\n\n\n\n\n"+os.getenv("PASSWORD"))
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    receiver = "charlieedoherty@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
