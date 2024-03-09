from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from api.v1.clients.services import get_client_email


@shared_task
def send_message_on_new_order(mysql_user_id):
    client_email = get_client_email(mysql_user_id)
    if client_email:
        send_mail(subject='new Order',
                  message='Hello New order for you',
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[client_email])


@shared_task
def send_message_on_less_limit(mysql_user_id, request_counts, limit):
    if limit - request_counts == settings.LESS_LIMIT_REQUEST:
        client_email = get_client_email(mysql_user_id=mysql_user_id)
        if client_email:
            send_mail(subject='Less Limit',
                      message=f'Hello Less Limit Packet ==> "{request_counts}" from "{limit}"',
                      from_email=settings.DEFAULT_FROM_EMAIL,
                      recipient_list=[client_email])