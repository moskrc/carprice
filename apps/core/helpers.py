from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(subject, template_file, context, to_email, from_email=None):
    html_body = render_to_string(template_file, context)
    text_body = strip_tags(html_body)

    msg = EmailMultiAlternatives(subject, text_body, from_email, to_email)
    msg.attach_alternative(html_body, "text/html")
    msg.send(fail_silently=True)
