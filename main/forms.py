from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxInput, EmailInput, Select, TextInput, DateInput, PasswordInput
from .models import Employees, Position, Education, News
from django.contrib.auth.forms import AuthenticationForm
from django.forms import DateTimeInput
from django.contrib.auth import authenticate, login



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


class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'employee']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "employee": Select(attrs={
                'class': 'form-control',
                'label': 'Employees'
            })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['password'].label = 'Пароль'
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе')
#         user = User.objects.filter(username=username).first()
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError("Неверный пароль")
#         return self.cleaned_data
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
