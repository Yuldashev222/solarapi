from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_email_order_accepted(email):
    send_mail(subject='hy', message='hy', from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[email])
