from django import forms

from vacancy_app.models import Application, Company


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
        fields = ('name', 'logo', 'location', 'description', 'employee_count')


