from django.db import models
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    salary = models.FloatField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, related_name='vacancy')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-salary',)
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

