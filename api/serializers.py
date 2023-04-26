from rest_framework import serializers
from . import models

class CompanySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"

class VacancySerializerV1(serializers.ModelSerializer):
    company = CompanySerializerV1()
    class Meta:
        model = models.Vacancy
        fields = "__all__"