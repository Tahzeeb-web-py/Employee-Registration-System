from django.shortcuts import render, redirect
from .forms import emp_forms
from .models import Employee

# Create your views here.
def emp_list(request):
    context={
        'employee_list':Employee.objects.all()
    }
    print(context)
    return render(request, "Registration/employee_list.html", context)
def emp_form(request):
    if request.method == "GET":
        form=emp_forms()
        return render(request, "Registration/employee_form.html", {'form':form})
    else:
        form=emp_forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
        

def emp_delete(request):
    return render(request, "Registration/employee_list.html")
