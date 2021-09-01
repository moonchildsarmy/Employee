# Generated by Django 3.0.8 on 2021-08-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Учебное заведение')),
                ('level', models.CharField(max_length=50, verbose_name='Уровень')),
                ('faculty', models.CharField(max_length=100, verbose_name='Факультет')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='Год окончания')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образовани',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Должность')),
                ('is_active', models.BooleanField(verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Изобрежения')),
                ('is_active', models.BooleanField(verbose_name='Активен')),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Education')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Position')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
