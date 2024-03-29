import requests
from django.conf import settings


def get_solar_api_info(latitude, longitude):
    params = {
        'key': settings.SOLAR_API_KEY,
        'requiredQuality': settings.SOLAR_API_REQUIRED_QUALITY,
        'location.latitude': latitude,
        'location.longitude': longitude
    }
    response = requests.get(url=settings.BUILDING_INSIGHTS, params=params)
    data = response.json()
    return data
