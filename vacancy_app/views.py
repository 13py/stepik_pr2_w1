from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .form import RegisterForm, ApplicationForm, MyCompanyForm, EditVacancyForm
from .models import Specialty, Company, Vacancy, Application


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
        print(request.user.id)
        vacancy_form = ApplicationForm(request.POST)
        vacancy = get_object_or_404(Vacancy, id=id)
        print(id)
        curent_user = request.user.id
        print(curent_user)
        user = User.objects.get(id=curent_user).id
        print(user)
        print('конец GET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        context = {
            'vacancy': vacancy,
            #'vacancy_form': vacancy_form,
            #'user': user
        }
        return render(request, 'vacancy_app/vacancy.html', context=context)

    def post(self, request, id):
        print('ПРИВЕТ', id)
        vacancy_form = ApplicationForm(request.POST)

        # print(vacancy_form)
        # print(request)
        # print(vacancy_form.is_valid())
        # print(vacancy_form.errors)
        curent_user = request.user.id
        # print('post curent_user ', curent_user)
        user = User.objects.get(id=curent_user).id
        vacancy = Vacancy.objects.filter(id=id).first().id
        # print('id', id)
        print(vacancy_form.is_valid())
        print(vacancy_form.fields.get('written_username'), 'user')
        # vacancy_form.fields['vacancy'] = id
        # vacancy_form.fields['user'] = request.user.id
        print(vacancy_form.fields.get('user'), 'user')
        # print(vacancy_form)
        print(vacancy_form.is_valid())
        print(vacancy_form.errors)
        print(request.user.id)
        print('вакансия',)

        if vacancy_form.is_valid():
            print('ВАЛИДАЦИЯ')
            vacancy_send = vacancy_form.cleaned_data
            print('vacancy', vacancy_send)
            print(vacancy_send['written_cover_letter'])
            print(Vacancy.objects.filter(id=id).first())
            print('vacancy_send', vacancy_send)
            vacancy_send['user'] = request.user
            vacancy_send['vacancy'] = vacancy
            print(vacancy_send)
            print(vacancy)
            Application.objects.create(written_username=vacancy_send['written_username'],
                                       written_phone=vacancy_send['written_phone'],
                                       written_cover_letter=vacancy_send['written_cover_letter'],
                                       user=vacancy_send['user'],
                                       vacancy=Vacancy.objects.get(id=id),
                                       )
        vacancy_id = id
        return redirect(f'/vacancies/{vacancy_id}/send')


class AboutView(View):
    def get(self, request):
        return render(request, 'vacancy_app/about.html')


class SentRequestView(View):
    def get(self, request, vacancy_id):
        context = {'id': vacancy_id}
        return render(request, 'vacancy_app/sent.html', context=context)


class MyCompanyView(View):
    def get(self, request):
        # print('мои компании', Company.objects.filter(owner=request.user))
        my_company = Company.objects.filter(owner=request.user).first()
        # print(my_company.id)
        # print(my_company.name)
        # print(my_company.location)
        # company_form = MyCompanyForm(request.POST)
        # print(request.method)
        if Company.objects.filter(owner=request.user):
            template = 'vacancy_app/company-edit.html'
            context = {'my_company': my_company}
            return render(request, template, context=context)
        else:
            template = 'vacancy_app/company-create.html'
            context = dict()
            return render(request, template, context=context)


    def post(self, request):
        company_form = MyCompanyForm(request.POST)
        print('company_form', company_form)
        print(company_form.is_valid())
        if company_form.is_valid():
            print('ВАЛИДАЦИЯ ПРОЙДЕНА')

            company_clear_data = company_form.cleaned_data
            print(company_clear_data)
            print(company_form.errors)
            my_company = Company.objects.filter(owner=request.user).first()
            print(my_company.description)
            my_company.name = company_clear_data['name']
            print(my_company.location, 'локация')
            my_company.location = company_clear_data['location']
            print(my_company.location)
            print('перед if')
            if company_clear_data['employee_count']:
                print('лого путь есть')
                print(my_company.logo)
                print(company_clear_data['employee_count'])
                #my_company.logo = company_clear_data['logo']
            my_company.employee_count = company_clear_data['employee_count']
            #my_company.owner = request.user
            my_company.save()
            print(my_company.employee_count)
        return redirect('main')



class MyCompanyVacanciesView(View):
    def get(self, request):
        polzovat = request.user
        print(polzovat, polzovat.id)
        my_company = Company.objects.filter(owner=request.user.id).first()
        print(my_company)
        print(my_company.id)
        my_vacancies = Vacancy.objects.filter(company=my_company.id)
        print(my_vacancies)
        context = {'my_vacancies': my_vacancies}
        return render(request, 'vacancy_app/vacancy-list.html', context=context)


class MyCompanyVacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.filter(id=vacancy_id).first()
        specialties = Specialty.objects.all()

        active_spec = vacancy.specialty
        print(active_spec.id)
        context = {'vacancy': vacancy,
                   'specialties': specialties,
                   'active_spec': active_spec}
        return render(request, 'vacancy_app/vacancy-edit.html', context=context)

    def post(self, request, vacancy_id):
        edit_vacancy = EditVacancyForm(request.POST)
        if edit_vacancy.is_valid():
            print('валидный')
            vacancy_cleaned = edit_vacancy.cleaned_data
            vacancy = Vacancy.objects.filter(id=vacancy_id).first()
            vacancy.title = vacancy_cleaned['title']
            vacancy.salary_min = vacancy_cleaned['salary_min']
            vacancy.salary_max = vacancy_cleaned['salary_max']
            vacancy.skills = vacancy_cleaned['skills']
            vacancy.description = vacancy_cleaned['description']
            vacancy.specialty = vacancy_cleaned['specialty']
            vacancy.save()

        return redirect('main')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'vacancy_app/login.html'

    # def post(self, request):
    #     return render(request, 'vacancy_app/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'vacancy_app/register.html' )

    def post(self, request):
        register_form = RegisterForm(request.POST)
        # print(register_form)
        # print(register_form.fields)
        if register_form.is_valid():
            data_register = register_form.cleaned_data
            # print(data_register)
            User.objects.create_user(username=data_register['login'],
                                     first_name=data_register['first_name'],
                                     last_name=data_register['last_name'],
                                     password=data_register['password'])
        return redirect('main')


class MyCompanyMakeView(View):
    def get(self, request):
        return render(request, 'vacancy_app/company-edit.html')

    def post(self, request):
        company_form = MyCompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.owner = request.user
            company.save()
            company_form.save()
        return redirect('main')


class MyVacancyCreate(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        context = {'specialties': specialties}
        return render(request, 'vacancy_app/vacancy-edit.html', context=context)

    def post(self, request):
        edit_vacancy_form = EditVacancyForm(request.POST)
        if edit_vacancy_form.is_valid():
            new_vacancy = edit_vacancy_form.save(commit=False)
            new_vacancy.company = Company.objects.filter(owner=request.user).first()
            new_vacancy.save()
            edit_vacancy_form.save()
        return redirect('main')

class MyLogoutView(LogoutView):
    pass


def my_handler404(request, exception=None):
    return render(request, '404.html')


def my_handler500(request, exception=None):
    return render(request, '500.html')
