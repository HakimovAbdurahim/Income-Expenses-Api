from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(email):
        email_data = EmailMessage(
            subject=email['email_subject'], body=email['email_body'], to=email['to_email'])
        email_data.send()
