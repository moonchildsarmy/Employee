from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponseNotFound
from django.views.generic import UpdateView
from .models import Education, Employees, Position
from .forms import AddEmployeeForm, UpdateEmployeeForm
from django.db.models import Q


def oops(request):
    return render(request, 'main/404.html')


def index(request):
    posts = Employees.objects.all()
    categories = Position.objects.all()
    education = Education.objects.all()

    return render(request, 'main/employees_list.html', {
        'posts': posts,
        'categories': categories,
        'education': education
    })


def add_employee(request):
    categories = Position.objects.all()
    education = Education.objects.all()
    if request.method == 'POST':

        form = AddEmployeeForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print(form)
            return redirect('index')
        # else:
        #     return redirect('add_review')
    else:
        form = AddEmployeeForm()
    return render(request, 'main/add_page.html', {
        'form': form,
        'categories': categories,
        'education': education
    })


def show_detail(request, id):
    categories = Position.objects.all()
    education = Education.objects.all()
    post = Employees.objects.get(id=id)

    return render(request, 'main/show_detail.html', {
        'post': post,
        'categories': categories,
        'education': education
    })


def delete(request, id):
    try:
        employee = Employees.objects.get(id=id)
        employee.delete()
        return redirect('index')
    except Employees.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def update_page(request, pk):
    info = Employees.objects.get(id=pk)
    form = AddEmployeeForm(instance=info)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('index')
    else:
        form = AddEmployeeForm()

    return render(request, 'main/edit_page.html', {
        'info': info,
        'form': AddEmployeeForm(instance=info)
    })


def sorting(request):
    employee = Employees.objects.order_by("first_name")
    print('keldi')

    return render(request, "main/employees_list.html", {"posts": employee})


def sorting_1(request):
    employee_1 = Employees.objects.order_by("-first_name")

    return render(request, "main/employees_list.html", {"posts": employee_1})


def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        f = Employees.objects.filter(Q(last_name__icontains=search_query) | Q(first_name__icontains=search_query))
    else:
        f = Employees.objects.all()

    return render(request, "main/employees_list.html", {"posts": f})


def category(request, id):
    education = Education.objects.all()
    categories = Position.objects.all()
    cate = Position.objects.get(id=id)
    queryset = Employees.objects.filter(position=cate)


    if queryset:
        c = {'posts': queryset,
             'categories': categories,
             'education': education
             }
        return render(request, 'main/employees_list.html', c)

    else:
        return render(request, 'main/employees_list.html')


def category_2(request, id):
    education = Education.objects.all()
    categories = Position.objects.all()
    edu = Education.objects.get(id=id)
    queryset = Employees.objects.filter(education=edu)


    if queryset:
        e = {'posts': queryset,
             'categories': categories,
             'education': education}

        return render(request, 'main/employees_list.html', e)

    else:
        return render(request, 'main/employees_list.html')

# Create your views here.
