from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty


def index(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("q7")
    else:
        form = FacultyForm()
    all_faculty = Faculty.objects.all()
    cse_prof = Faculty.objects.filter(
        branch__iexact="CSE", title__iexact="Professor")
    return render(request, "q7/index.html", {"form": form, "all_faculty": all_faculty, "cse_prof": cse_prof})
