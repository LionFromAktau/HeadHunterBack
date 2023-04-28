from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/vacancies/submitted/<company_id>/', consumers.VacancyConsumer.as_asgi()),
]