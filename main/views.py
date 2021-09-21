from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponseNotFound
from django.views.generic import UpdateView
from .models import Education, Employees, Position, Dismissal
from .forms import AddEmployeeForm, AddPositionForm, AddEducationForm, WhyDeleteForm
from django.db.models import Q


def oops(request):
    return render(request, 'main/employee_list/404.html')


def index(request):
    posts = Employees.objects.filter(is_active=True)
    categories = Position.objects.all()
    education = Education.objects.all()
    why = Dismissal.objects.all()

    return render(request, 'main/employee_list/employee.html', {
        'posts': posts,
        'categories': categories,
        'why': why,
        'education': education
    })


def add_employee(request):
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
    return render(request, 'main/employee_list/edit_form.html', {
        'form': form,
    })


def show_detail(request, id):
    post = Employees.objects.get(id=id)

    return render(request, 'main/employee_list/detail.html', {
        'post': post,
    })


def list_delete(request):
    delete = Employees.objects.filter(is_active=False)

    return render(request, 'main/employee_list/why_delete.html', {
        'delete': delete,
    })

def why_delete(request, id):
    employee = Employees.objects.get(id=id)
    employee.is_active = False
    employee.why_id = request.POST['why']
    employee.save()
    return redirect('index')


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

    return render(request, 'main/employee_list/edit_form.html', {
        'info': info,
        'form': AddEmployeeForm(instance=info)
    })


def sorting(request):
    education = Education.objects.all()
    categories = Position.objects.all()
    why = Dismissal.objects.all()
    employee = Employees.objects.order_by("first_name")


    return render(request, "main/employee_list/employee.html", {
        "posts": employee,
        "education": education,
        "categories": categories,
        "why": why
    })


def sorting_1(request):
    education = Education.objects.all()
    categories = Position.objects.all()
    why = Dismissal.objects.all()
    employee_1 = Employees.objects.order_by("-first_name")

    return render(request, "main/employee_list/employee.html", {
        "posts": employee_1,
        "education": education,
        "categories": categories,
        "why": why
    })


def search(request):
    education = Education.objects.all()
    categories = Position.objects.all()
    why = Dismissal.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        f = Employees.objects.filter(Q(last_name__icontains=search_query) | Q(first_name__icontains=search_query))
    else:
        f = Employees.objects.all()

    return render(request, "main/employee_list/employee.html", {
        "posts": f,
        "education": education,
        "categories": categories,
        "why": why
    })


def category(request, id):
    education = Education.objects.all()
    categories = Position.objects.all()
    why = Dismissal.objects.all()
    cate = Position.objects.get(id=id)
    queryset = Employees.objects.filter(position=cate)

    if queryset:
        c = {'posts': queryset,
             'categories': categories,
             'education': education,
             'why': why
             }
        return render(request, 'main/employee_list/employee.html', c)

    else:
        return render(request, 'main/employee_list/employee.html')


def category_2(request, id):
    education = Education.objects.all()
    categories = Position.objects.all()
    why = Dismissal.objects.all()
    edu = Education.objects.get(id=id)
    queryset = Employees.objects.filter(education=edu)

    if queryset:
        e = {'posts': queryset,
             'categories': categories,
             'education': education,
             'why': why
             }

        return render(request, 'main/employee_list/employee.html', e)

    else:
        return render(request, 'main/employee_list/employee.html')


def position(request):
    list = Position.objects.all()


    return render(request, 'main/employee_list/position_list.html',{
        'list': list,
    })


def add_position(request):
    if request.method == 'POST':

        form = AddPositionForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('position')
    else:
        form = AddPositionForm()
    return render(request, 'main/employee_list/position_list.html', {
        'form': form,
    })


def delete_position(request, id):
    try:
        positions = Position.objects.get(id=id)
        positions.delete()
        return redirect('position')
    except Position.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")

def education(request):
    lists = Education.objects.all()

    return render(request, 'main/employee_list/education_list.html',{
        'lists': lists,
    })


def add_education(request):
    if request.method == 'POST':

        form = AddEducationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('education')
    else:
        form = AddPositionForm()
    return render(request, 'main/employee_list/education_list.html', {
        'form': form,
    })


def delete_education(request, id):
    try:
        educations = Education.objects.get(id=id)
        educations.delete()
        return redirect('education')
    except Education.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")

# Create your views here.
