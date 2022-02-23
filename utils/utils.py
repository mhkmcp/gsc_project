from pickle import FALSE
from django.core.mail import EmailMessage
import threading


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_sailently=False)


class Util:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(
            subject=data["subject"], body=data["body"], to=[data["email_to"]]
        )
        EmailThread(email).start()
