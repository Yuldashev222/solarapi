from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import mysql.connector


def get_client_email(mysql_user_id):
    connection = mysql.connector.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                         password=settings.MYSQL_PASSWORD, database=settings.MYSQL_DATABASE)
    user_table = settings.MYSQL_USER_TABLE
    if connection.is_connected():
        cursor = connection.cursor()
        query = f'SELECT user_email FROM {user_table} WHERE ID = {mysql_user_id}'
        cursor.execute(query)
        temp = cursor.fetchone()
        cursor.close()
        connection.close()
        if temp is not None:
            return temp[0]

    return None
