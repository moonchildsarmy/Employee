from main.models import Position
from django.contrib import admin
from .models import Position, Education, Employees

admin.site.register(Position)
admin.site.register(Education)
admin.site.register(Employees)

# Register your models here.
