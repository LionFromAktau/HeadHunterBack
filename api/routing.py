from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/vacancies/submitted/', consumers.VacancyConsumer.as_asgi()),
]