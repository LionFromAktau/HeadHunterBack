from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from . import models, serializers, signals

class CompanyViewV1(ModelViewSet):
    serializer_class = serializers.CompanySerializerV1
    queryset = models.Company.objects.all()

    @action(detail=True, methods=['get'])
    def vacancies(self, request, pk):
        company = self.get_object()
        vacancies = models.Vacancy.objects.filter(company=company)
        serializer = serializers.VacancySerializerV1(vacancies,many=True)
        return Response(serializer.data)

class VacancyViewV1(ModelViewSet):
    serializer_class = serializers.VacancySerializerV1
    queryset = models.Vacancy.objects.all()

    @action(detail=True, methods=['get'])
    def submitted(self, request, pk):
        signals.vacancy_submitted.send(sender=models.Vacancy, instance=self.get_object())
        return Response({
            'message': 'vacancy submitted to the channel ws://127.0.0.1:8000/ws/vacancies/submitted/'
                         })

    @action(detail=False, methods=['get'])
    def top_ten(self, request):
        vacancies = models.Vacancy.objects.all()
        serializer = self.get_serializer(vacancies, many=True)
        return Response(serializer.data[:10])
