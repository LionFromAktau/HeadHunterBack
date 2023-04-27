from rest_framework import serializers
from . import models

class CompanySerializerV1(serializers.ModelSerializer):
    vacancies_number = serializers.IntegerField()
    class Meta:
        model = models.Company
        fields = "__all__"

class VacancySerializerV1(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    class Meta:
        model = models.Vacancy
        fields = "__all__"

    def get_company(self, obj):
        return obj.company.name