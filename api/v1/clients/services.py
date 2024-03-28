from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import mysql.connector


def get_client_limit(mysql_user_id):
    connection = mysql.connector.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                         password=settings.MYSQL_PASSWORD, database=settings.MYSQL_DATABASE)

    order_table = settings.MYSQL_ORDER_TABLE
    customer_table = settings.MYSQL_CUSTOMER_TABLE
    product_table = settings.MYSQL_PRODUCT_TABLE
    expire_days = settings.ORDER_EXPIRE_DAYS
    if connection.is_connected():
        cursor = connection.cursor()
        query = (f'SELECT SUM(p.sku) FROM {order_table} AS t '
                 f'JOIN {customer_table} AS c ON t.customer_id = c.customer_id '
                 f'JOIN {product_table} AS p ON t.product_id = p.product_id '
                 f'WHERE DATE_ADD(t.date_created, INTERVAL {expire_days} DAY) >= NOW() '
                 f'AND c.user_id = {mysql_user_id}')

        cursor.execute(query)
        temp = cursor.fetchone()
        cursor.close()
        connection.close()
        return temp[0] if temp[0] is not None else 0
    return False


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


def get_client_discounts(mysql_user_id):
    connection = mysql.connector.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                         password=settings.MYSQL_PASSWORD, database=settings.MYSQL_DATABASE)
    user_table = settings.MYSQL_USER_TABLE
    if connection.is_connected():
        cursor = connection.cursor()
        query = f'SELECT discount_name, discount_percent, discount_max_price, discount_service_name, discount_service, discount_service_max_price FROM {user_table} WHERE ID = {mysql_user_id}'
        cursor.execute(query)
        temp = cursor.fetchone()
        cursor.close()
        connection.close()
        discount_product = {
            'name': temp[0],
            'percent': temp[1],
            'max_price': temp[2]
        }
        discount_service = {
            'name': temp[3],
            'percent': temp[4],
            'max_price': temp[5]
        }
        if discount_service['percent'] is None:
            discount_service = None
        elif discount_service['percent'] <= 0:
            discount_service = None

        if discount_product['percent'] is None:
            discount_product = None
        if discount_product['percent'] <= 0:
            discount_product = None
        return discount_product, discount_service

    return None, None
