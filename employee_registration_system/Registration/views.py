from django.shortcuts import render
from .forms import emp_forms

# Create your views here.
def emp_list(request):
    return render(request, "Registration/employee_list.html")
def emp_form(request):
    form=emp_forms()
    return render(request, "Registration/employee_form.html", {'form':form})
def emp_delete(request):
    return render(request, "Registration/employee_list.html")
