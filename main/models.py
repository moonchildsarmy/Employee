from django.db import models
from datetime import date
from django.db.models.deletion import SET_NULL

from django.urls import reverse



class Position(models.Model):
    name = models.CharField("Должность", max_length=50)
    is_active = models.BooleanField("Активен", default=True)

    def str(self):
        return self.name
    

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"



class Education(models.Model):
    name = models.CharField("Учебное заведение", max_length=100)
    level = models.CharField("Уровень", max_length=50)
    faculty = models.CharField("Факультет", max_length=100)
    year = models.PositiveSmallIntegerField("Год окончания", default=2020)

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образовани"



class Employees(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    birthday = models.DateField("День рождения")
    phone = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField("Email", max_length=200, null=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True, verbose_name="Выбор учебного заведения", )
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name="Выбор должности")
    start_date = models.DateField("Дата входа на работу",null=True)
    salary = models.PositiveIntegerField("Заработная плата", help_text="указывать сумму в сомах", null=True)
    image = models.ImageField("Изобрежения", upload_to="images/", null=True)
    is_active = models.BooleanField("Активен", default=True)

    def str(self):
        return self.first_name

    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


# Create your models here.
