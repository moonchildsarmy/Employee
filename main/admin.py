from main.models import Position
from django.contrib import admin
from .models import Position, Education, Employees

class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = ['name', 'level', 'faculty', 'year']


class PositionAdmin(admin.ModelAdmin):
    model = Position
    list_display = ['name', 'is_active']


class EmployeesAdmin(admin.ModelAdmin):
    model = Employees
    list_display = ['first_name', 'last_name', 'birthday', 'phone', 'email', 'start_date', 'salary', 'is_active']

admin.site.register(Position, PositionAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Employees, EmployeesAdmin)



# Register your models here.
