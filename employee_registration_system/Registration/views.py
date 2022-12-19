from django.shortcuts import render, redirect
from .forms import emp_forms
from .models import Employee

# Create your views here.
def emp_list(request):
    context={
        'employee_list':Employee.objects.all()
    }
    
    return render(request, "Registration/employee_list.html", context)
def emp_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=emp_forms()
        else:
            employee=Employee.objects.get(pk=id)
            form = emp_forms(instance=employee)
        return render(request, "Registration/employee_form.html", {'form':form})
    else:
        if id ==0:
            form=emp_forms(request.POST)
        else:           
            employee=Employee.objects.get(pk=id)
            form=emp_forms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
        

def emp_delete(request, id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
