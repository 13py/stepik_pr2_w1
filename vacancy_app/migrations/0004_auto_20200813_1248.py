# Generated by Django 3.0.8 on 2020-08-13 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancy_app', '0003_auto_20200808_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_job', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo'),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=0, max_digits=10)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('portfolio', models.CharField(max_length=200)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy_app.Grade')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy_app.Specialty')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy_app.Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]