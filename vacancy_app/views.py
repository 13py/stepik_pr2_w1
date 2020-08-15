from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views import View

from .form import RegisterForm, ApplicationForm, MyCompanyForm, EditVacancyForm, SearchForm, ResumeForm
from .models import Specialty, Company, Vacancy, Application, Status, Grade, Resume


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
        name = get_object_or_404(Specialty, code=cat)
        vacancies = Vacancy.objects.filter(specialty__code=cat)
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
        vacancy_form = ApplicationForm(request.POST)
        vacancy = get_object_or_404(Vacancy, id=id)
        context = {
            'vacancy': vacancy,
            'vacancy_form': vacancy_form
        }
        return render(request, 'vacancy_app/vacancy.html', context=context)

    def post(self, request, id):
        vacancy_form = ApplicationForm(request.POST)
        vacancy = get_object_or_404(Vacancy, id=id)
        if vacancy_form.is_valid():
            vacancy_send = vacancy_form.cleaned_data
            vacancy_send['user'] = request.user
            vacancy_send['vacancy'] = vacancy.id
            Application.objects.create(written_username=vacancy_send['written_username'],
                                       written_phone=vacancy_send['written_phone'],
                                       written_cover_letter=vacancy_send['written_cover_letter'],
                                       user=vacancy_send['user'],
                                       vacancy=vacancy)
        vacancy_id = id
        return redirect(f'/vacancies/{vacancy_id}/send')


class AboutView(View):
    def get(self, request):
        return render(request, 'vacancy_app/about.html')


class SentRequestView(View):
    def get(self, request, vacancy_id):
        context = {
            'id': vacancy_id
        }
        return render(request, 'vacancy_app/sent.html', context=context)


class MyCompanyView(View):
    def get(self, request):
        my_company = get_object_or_404(Company, owner=request.user)
        if Company.objects.filter(owner=request.user):
            template = 'vacancy_app/company-edit.html'
            context = {
                'my_company': my_company
            }
            return render(request, template, context=context)
        else:
            template = 'vacancy_app/company-create.html'
            context = dict()
            return render(request, template, context=context)

    def post(self, request):
        company_form = MyCompanyForm(request.POST)
        if company_form.is_valid():
            company_clear_data = company_form.cleaned_data
            my_company = get_object_or_404(Company, owner=request.user)
            my_company.name = company_clear_data['name']
            my_company.location = company_clear_data['location']
            my_company.employee_count = company_clear_data['employee_count']
            my_company.save()
        return redirect('main')


class MyCompanyVacanciesView(View):
    def get(self, request):
        my_company = get_object_or_404(Company, owner=request.user.id)
        my_vacancies = Vacancy.objects.filter(company=my_company.id)
        context = {
            'my_vacancies': my_vacancies
        }
        return render(request, 'vacancy_app/vacancy-list.html', context=context)


class MyCompanyVacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        specialties = Specialty.objects.all()
        active_spec = vacancy.specialty
        applications = vacancy.applications.all()
        applications_count = applications.count()
        context = {
            'vacancy': vacancy,
            'specialties': specialties,
            'active_spec': active_spec,
            'applications': applications,
            'applications_count': applications_count
        }
        return render(request, 'vacancy_app/vacancy-edit.html', context=context)

    def post(self, request, vacancy_id):
        edit_vacancy = EditVacancyForm(request.POST)
        if edit_vacancy.is_valid():
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


class RegisterView(View):
    def get(self, request):
        return render(request, 'vacancy_app/register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            data_register = register_form.cleaned_data
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
        context = {
            'specialties': specialties
        }
        return render(request, 'vacancy_app/vacancy-edit.html', context=context)

    def post(self, request):
        edit_vacancy_form = EditVacancyForm(request.POST)
        if edit_vacancy_form.is_valid():
            new_vacancy = edit_vacancy_form.save(commit=False)
            new_vacancy.company = Company.objects.filter(owner=request.user).first()
            new_vacancy.save()
            edit_vacancy_form.save()
        return redirect('main')


class SearchView(View):
    def get(self, request):
        search = SearchForm(request.GET)
        if search.is_valid():
            search_request = search.cleaned_data.get('s')
            searches = Vacancy.objects.all()
            vacancies = searches.filter(Q(title__contains=search_request) | Q(description__contains=search_request))
            result = vacancies.exists()
        context = {
            'search_request': search_request,
            'vacancies': vacancies,
            'result': result
        }
        return render(request, 'vacancy_app/search.html', context=context)


class MyResumeView(View):
    def get(self, request):
        try:
            request.user.resume
            resume = Resume.objects.filter(user=request.user).first()
            statuses = Status.objects.all()
            grades = Grade.objects.all()
            specialties = Specialty.objects.all()
            context = {
                'resume': resume,
                'statuses': statuses,
                'grades': grades,
                'specialties': specialties
            }
            template = 'vacancy_app/resume-edit.html'
        except User.resume.RelatedObjectDoesNotExist:
            template = 'vacancy_app/resume-create.html'
            context = {}
        return render(request, template, context=context)

    def post(self, request):
        my_resume = ResumeForm(request.POST)
        if my_resume.is_valid():
            clear_resume = my_resume.cleaned_data
            resume = Resume.objects.filter(user=request.user).first()
            resume.name = clear_resume.get('name')
            resume.surname = clear_resume.get('surname')
            resume.status = clear_resume.get('status')
            resume.salary = clear_resume.get('salary')
            resume.specialty = clear_resume.get('specialty')
            resume.grade = clear_resume.get('grade')
            resume.education = clear_resume.get('education')
            resume.experience = clear_resume.get('experience')
            resume.portfolio = clear_resume.get('portfolio')
            resume.save()
        return redirect('main')


class MyResumeCreateView(View):
    def get(self, request):
        statuses = Status.objects.all()
        grades = Grade.objects.all()
        specialties = Specialty.objects.all()
        context = {
            'statuses': statuses,
            'grades': grades,
            'specialties': specialties
        }
        return render(request, 'vacancy_app/resume-edit.html', context=context)

    def post(self, request):
        my_resume = ResumeForm(request.POST)
        if my_resume.is_valid():
            resume = my_resume.save(commit=False)
            resume.user = request.user
            my_resume.save()
        return redirect('main')


class MyLogoutView(LogoutView):
    pass


def my_handler404(request, exception=None):
    return render(request, '404.html')


def my_handler500(request, exception=None):
    return render(request, '500.html')
