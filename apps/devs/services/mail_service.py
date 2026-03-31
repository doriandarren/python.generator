from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class SendMailService:

    def __init__(self, subject, to_emails, from_email=None):
        self.subject = subject
        self.to_emails = [to_emails] if isinstance(to_emails, str) else to_emails
        self.from_email = from_email or settings.DEFAULT_FROM_EMAIL
        self.template_html = "emails/test_email.html"

    def send_html_mail(self, title, body):
        html_content = render_to_string(self.template_html, {
            "title": title,
            "body": body,
        })

        msg = EmailMultiAlternatives(
            subject=self.subject,
            body="",
            from_email=self.from_email,
            to=self.to_emails,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return True