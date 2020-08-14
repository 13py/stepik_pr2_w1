from django import forms

from vacancy_app.models import Application, Company, Vacancy


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')


class MyCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count')


class EditVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title',
                  'specialty',
                  'skills',
                  'description',
                  'salary_min',
                  'salary_max')


class SearchForm(forms.Form):
    s = forms.CharField()
