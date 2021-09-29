from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponseNotFound, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Education, Employees, Position, Dismissal, News
from .forms import AddEmployeeForm, AddPositionForm, AddEducationForm, NewsAddForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}

    return render(request, 'main/employee_list/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/employee_list/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')


def oops(request):
    return render(request, 'main/employee_list/404.html')

@login_required(login_url='login')
def index(request):
    posts = Employees.objects.filter(is_active=True)
    categories = Position.objects.all()
    education = Education.objects.all()
    why = Dismissal.objects.all()


    return render(request, 'main/employee_list/employee.html', {
        'posts': posts,
        'categories': categories,
        'why': why,
        'education': education,
    })

@login_required(login_url='login')
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

@login_required(login_url='login')
def show_detail(request, id):
    post = Employees.objects.get(id=id)

    return render(request, 'main/employee_list/detail.html', {
        'post': post,
    })

@login_required(login_url='login')
def list_delete(request):
    delete = Employees.objects.filter(is_active=False)

    return render(request, 'main/employee_list/why_delete.html', {
        'delete': delete,
    })


@login_required(login_url='login')
def why_delete(request, id):
    employee = Employees.objects.get(id=id)
    employee.is_active = False
    employee.why_id = request.POST['why']
    employee.save()
    return redirect('index')


@login_required(login_url='login')
def delete(request, id):
    try:
        employee = Employees.objects.get(id=id)
        employee.delete()
        return redirect('index')
    except Employees.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def position(request):
    list = Position.objects.all()


    return render(request, 'main/employee_list/position_list.html',{
        'list': list,
    })


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_position(request, id):
    try:
        positions = Position.objects.get(id=id)
        positions.delete()
        return redirect('position')
    except Position.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


@login_required(login_url='login')
def education(request):
    lists = Education.objects.all()

    return render(request, 'main/employee_list/education_list.html',{
        'lists': lists,
    })


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_education(request, id):
    try:
        educations = Education.objects.get(id=id)
        educations.delete()
        return redirect('education')
    except Education.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


@login_required(login_url='login')
def news_list(request):
    card = News.objects.all()

    return render(request, 'main/employee_list/news_list.html', {
        'card': card,
    })


@login_required(login_url='login')
def news_detail(request, id):
    cards = News.objects.get(id=id)

    return render(request, 'main/employee_list/news_detail.html', {
        'cards': cards,
    })


@login_required(login_url='login')
def add_news(request):
    if request.method == 'POST':

        form = NewsAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('news_list')
    else:
        form = NewsAddForm()
    return render(request, 'main/employee_list/add_news.html', {
        'form': form,
    })

# Create your views here.
