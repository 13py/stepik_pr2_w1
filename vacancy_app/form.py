from django import forms
from django.forms import TextInput, Textarea

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
                               widget=forms.PasswordInput(attrs={
                                     'class': 'form-control',
                                     'id': 'inputPassword',
                                     'type': 'password'}))


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')
        widgets = {
            'written_username': TextInput(attrs={'class': 'form-control', 'id': 'userName', 'minlength': 3}),
            'written_phone': TextInput(attrs={'class': 'form-control', 'id': 'userPhone'}),
            'written_cover_letter': Textarea(attrs={'class': 'form-control', 'id': 'userMsg', 'rows': '8'})
        }


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
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'userName', 'minlength': 3}),
        #     'surname': forms.TextInput(attrs={'class': 'form-control', 'id': 'userPhone'}),
        #     'status': forms.Select(attrs={'class': 'custom-select mr-sm-2', 'id': 'userReady'}),
        #     'salary': forms.NumberInput(attrs={'class': 'form-control', 'id': 'userPortfolio'}),
        #     'specialty': forms.Select(attrs={'class': 'custom-select mr-sm-2', 'id': 'userSpecialization'}),
        #     'grade': forms.Select(attrs={'class': 'custom-select mr-sm-2', 'id': 'userQualification'}),
        #     'education': forms.Textarea(attrs={'class': 'form-control text-uppercase', 'id': 'userEducation',
        #                                        'rows': '4'}),
        #     'experience': forms.Textarea(attrs={'class': 'form-control', 'id': 'userExperience', 'rows': '4'}),
        #     'portfolio': forms.URLInput(attrs={'class': 'form-control', 'id': 'userPortfolio', 'rows': '4',
        #                                        'placeholder': "http://anylink.github.io"})
        # }
