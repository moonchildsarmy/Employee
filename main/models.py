from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models.deletion import SET_NULL

from django.urls import reverse


User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]



class Position(models.Model):
    name = models.CharField("Должность", max_length=50)
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"



class Education(models.Model):
    name = models.CharField("Учебное заведение", max_length=100)
    level = models.CharField("Уровень", max_length=50)
    faculty = models.CharField("Факультет", max_length=100)
    year = models.PositiveSmallIntegerField("Год окончания", default=2020)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образовании"


class Dismissal(models.Model):
    name = models.CharField("Причина увольнения", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Причина"
        verbose_name_plural = "Причины"


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
    why = models.ForeignKey(Dismissal, on_delete=models.SET_NULL, null=True, verbose_name="Причина увольнения")

    def __str__(self):
        return self.first_name

    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class News(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    text = models.CharField("Текст статьи", max_length=500)
    image = models.ImageField("Изобрежения", upload_to="images/", null=True)
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, verbose_name="Сотрудник")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# Create your models here.
