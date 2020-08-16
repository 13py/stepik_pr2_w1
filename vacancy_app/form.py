from django import forms

from vacancy_app.models import Application, Company, Vacancy, Resume


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=15,
                            min_length=3,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'id': 'inputLogin',
                                'type': 'text',
                                'required autofocus': ''}))
    first_name = forms.CharField(max_length=30,
                                 min_length=3,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'id': 'inputName',
                                     'type': 'text'}))

    last_name = forms.CharField(max_length=30,
                                min_length=3,
                                widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'id': 'inputSurname',
                                     'type': 'text'}))
    password = forms.CharField(max_length=30,
                               min_length=5,
                               widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'id': 'inputPassword',
                                     'type': 'password'}))


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


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name',
                  'surname',
                  'status',
                  'salary',
                  'specialty',
                  'grade',
                  'education',
                  'experience',
                  'portfolio')
