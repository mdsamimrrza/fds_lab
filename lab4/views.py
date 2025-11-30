from django.shortcuts import render, redirect
from .forms import employeeForms
from .models import employeeDetail


def index(request):
    if request.method == "POST":
        form = employeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("q4")
    else:
        form = employeeForms()
    employees = employeeDetail.objects.all()
    high_salary = employeeDetail.objects.filter(salary__gt=50000)
    return render(request, "q4/index.html", {"form": form, "employees": employees, "high_salary": high_salary})
