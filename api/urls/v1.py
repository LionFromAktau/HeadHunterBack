from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewV1)
router.register(r'vacancies', views.VacancyViewV1)
urlpatterns = router.urls