from django import forms
from django.db.models.fields import BooleanField
from django.forms.widgets import CheckboxInput, EmailInput, RadioSelect, Select, TextInput, DateInput, NullBooleanSelect
from .models import Employees, Position, Education
from django.forms import DateTimeInput



class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'birthday', 'phone', 'email', 'education', 'position', 'start_date', 'salary', 'image', 'is_active']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "birthday": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'День рождения',
            }),
            # "birthday": forms.SelectDateWidget(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'День рождения',
            #     'choices': 'BIRTH_YEAR_CHOICES'
            # }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "education": Select(attrs={
                'class': 'form-control',
                'label':'Education'
            }),
            "position": Select(attrs={
                'class': 'form-control',
                'label':'Position'
            }),
            "start_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выхода на работу'
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата'
            }),
            "is_active": CheckboxInput()
        }

class AddPositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = [ 'name', 'is_active']

        widgets = {
            "name" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "is_active": CheckboxInput()
        }


class AddEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [ 'name', 'level', 'faculty', 'year']

        widgets = {
            "name" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Университет'
            }),
            "faculty": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Факультет'
            }),
            "faculty": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уровень'
            }),
            "year": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год окончания'
            }),
        }


class WhyDeleteForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['why']


