from django.contrib import admin
from . import models

class CompanyVacancyInline(admin.TabularInline):
    model = models.Vacancy
    extra = 1
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'city')
    inlines = (CompanyVacancyInline,)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'salary', 'company')


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Vacancy, VacancyAdmin)
