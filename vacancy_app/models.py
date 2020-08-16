from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(upload_to='logo', blank=True)
    description = models.TextField(blank=True)
    employee_count = models.IntegerField(blank=True, null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='specialties', blank=True)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=0)
    salary_max = models.DecimalField(max_digits=10, decimal_places=0)
    published_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=100)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, related_name="applications", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="applications", on_delete=models.CASCADE, null=True)


class Status(models.Model):
    status_job = models.CharField(max_length=50)

    def __str__(self):
        return self.status_job


class Grade(models.Model):
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.qualification


class Resume(models.Model):
    user = models.OneToOneField(User, related_name='resume', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=0)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.CharField(max_length=200)
