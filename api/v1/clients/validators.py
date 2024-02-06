import validators
import mysql.connector
from django.conf import settings

from api.v1.solarapiinfos.models import SolarInfo


def validate_domain(domain):
    validators.domain(domain)


def client_limit_exists(customer_id):
    # solar_api_requests = SolarInfo.objects.filter(customer_id=customer_id).count()
    connection = mysql.connector.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                         password=settings.MYSQL_PASSWORD, database=settings.MYSQL_DATABASE_NAME)

    table_name = settings.MYSQL_ORDER_TABLE_NAME
    expire_days = settings.ORDER_EXPIRE_DAYS
    if connection.is_connected():
        cursor = connection.cursor()
        query = (f'SELECT EXISTS (SELECT * FROM {table_name} '
                 f'WHERE '
                 f'DATE_ADD(date_created, INTERVAL {expire_days} DAY) >= NOW() '
                 f'AND '
                 f'customer_id = {customer_id})')
                 # f'AND '
                 # f'limit > {solar_api_requests})')
        cursor.execute(query)
        temp = cursor.fetchone()
        cursor.close()
        connection.close()
        return bool(temp[0])
    return False
