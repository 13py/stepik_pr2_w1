# Generated by Django 3.0.8 on 2020-08-01 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('employee_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, upload_to='specialties')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('skills', models.TextField()),
                ('description', models.TextField()),
                ('salary_min', models.DecimalField(decimal_places=0, max_digits=10)),
                ('salary_max', models.DecimalField(decimal_places=0, max_digits=10)),
                ('published_at', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancy_app.Company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancy_app.Specialty')),
            ],
        ),
    ]
