from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

from .models import Specialty, Company, Vacancy


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()
        context = {
            'specialties': specialties,
            'companies': companies
        }
        return render(request, 'vacancy_app/index.html', context=context)


class VacancyListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies
        }
        return render(request, 'vacancy_app/vacancies.html', context=context)


class VacancySpecView(View):
    def get(self, request, cat):
        get_object_or_404(Specialty, code=cat)
        vacancies = Vacancy.objects.filter(specialty__code=cat)
        name = Specialty.objects.filter(code=cat).first()
        context = {
            'vacancies': vacancies,
            'name': name
        }
        return render(request, 'vacancy_app/vacancies_cat.html', context=context)


class CardCompanyView(View):
    def get(self, request, id):
        company = get_object_or_404(Company, id=id)
        vacancies = Vacancy.objects.filter(company__id=id)
        context = {
            'company': company,
            'vacancies': vacancies
        }
        return render(request, 'vacancy_app/company.html', context=context)


class VacancyView(View):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, id=id)
        context = {
            'vacancy': vacancy
        }
        return render(request, 'vacancy_app/vacancy.html', context=context)


class AboutView(View):
    def get(self, request):
        return render(request, 'vacancy_app/about.html')


def my_handler404(request, exception=None):
    return render(request, '404.html')


def my_handler500(request, exception=None):
    return render(request, '500.html')
