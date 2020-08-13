"""jundev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from vacancy_app.views import AboutView, MyVacancyCreate
from vacancy_app.views import CardCompanyView
from vacancy_app.views import MainView
from vacancy_app.views import MyCompanyMakeView
from vacancy_app.views import MyCompanyVacanciesView
from vacancy_app.views import MyCompanyVacancyView
from vacancy_app.views import MyCompanyView
from vacancy_app.views import MyLoginView
from vacancy_app.views import MyLogoutView
from vacancy_app.views import RegisterView
from vacancy_app.views import SentRequestView
from vacancy_app.views import VacancyListView
from vacancy_app.views import VacancySpecView
from vacancy_app.views import VacancyView
from vacancy_app.views import my_handler404
from vacancy_app.views import my_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:vacancy_id>/send', SentRequestView.as_view(), name='send'),
    path('vacancies/cat/<str:cat>/', VacancySpecView.as_view(), name='vacancies_cat'),
    path('companies/<int:id>/', CardCompanyView.as_view(), name='companies'),
    path('vacancies/<int:id>/', VacancyView.as_view(), name='vacancy'),
    path('about/', AboutView.as_view(), name='about'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/make/', MyCompanyMakeView.as_view(), name='company_make'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyCompanyVacancyView.as_view(), name='company-edit'),
    path('mycompany/create-vacancy/', MyVacancyCreate.as_view(), name='create-vacancy'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('myresume/', name='myresume'),
    path('search/', name='search')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = my_handler404
handler500 = my_handler500
