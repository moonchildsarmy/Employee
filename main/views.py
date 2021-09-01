from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Employees
from .forms import AddEmployeeForm


# class home(ListView):
#     model = Employees
#     template_name = 'main/employees_list.html '
#     context_object_name = 'posts'


def index(request):
    posts = Employees.objects.all()

    return render(request, 'main/employees_list.html', {
        'posts': posts, 
    })


def add_employee(request):
    if request.method =='POST':
        
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
    return render(request, 'main/add_page.html', {'form' : form,})


def oops(request):
    return render(request, 'main/404.html')

def show_detail(request, id):
    post = Employees.objects.get(id=id)


    return render(request, 'main/show_detail.html', {'post':post })
    # post = get_object_or_404(Employees, pk=post_id)

    # context = {

    #     'post': post
    # }

    # return render(request, 'main/show_detail.html', context=context )


# class addpage(CreateView):
#     form_class = AddEmployeeForm
#     template_name = 'main/add_page.html'
#     success_url = reverse_lazy('home_11')











# def employee(request):
#     employee = Employees.objects.all()
#     print(employee[0].image.url)
#     return render(request, 'main/EmployeeList.html', {
#         'employee': employee, 
#     })
# Create your views here.
