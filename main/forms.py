from django import forms
from django.db.models.fields import BooleanField
from django.forms.widgets import EmailInput, Select, TextInput
from .models import Employees
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
            "birthday": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'День рождения'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "start_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выхода на работу'
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата'
            }),
        }