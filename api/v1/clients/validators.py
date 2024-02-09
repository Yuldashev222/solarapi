import validators
import mysql.connector
from django.conf import settings

from api.v1.clients.tasks import send_message_on_less_limit
from api.v1.solarapiinfos.models import SolarInfo


def validate_domain(domain):
    validators.domain(domain)


def client_exists(mysql_user_id, domain):
    connection = mysql.connector.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                         password=settings.MYSQL_PASSWORD, database=settings.MYSQL_DATABASE)
    user_table = settings.MYSQL_USER_TABLE

    if connection.is_connected():
        cursor = connection.cursor()

        query = f'SELECT EXISTS (SELECT * FROM {user_table} WHERE ID = {mysql_user_id})'  # last  AND domain = "{domain}"

        cursor.execute(query)
        temp = cursor.fetchone()
        cursor.close()
        connection.close()
        return bool(temp[0])
    return False


def client_limit_exists(mysql_user_id):
    solar_api_requests = SolarInfo.objects.filter(mysql_user_id=mysql_user_id, success=True).count()
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
        bol = temp[0] > solar_api_requests
        # if bol:
        #     send_message_on_less_limit.delay(mysql_user_id=mysql_user_id,
        #                                      request_counts=solar_api_requests,
        #                                      limit=temp[0])
        return bol
    return False
