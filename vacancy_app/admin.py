from django.contrib import admin
from .models import Company, Vacancy, Specialty, Application


class CompanyAdmin(admin.ModelAdmin):
    pass


class VacancyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
