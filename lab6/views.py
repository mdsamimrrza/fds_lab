from django.shortcuts import render, redirect
from .forms import PlacementForm
from .models import Placement


def index(request):
    if request.method == "POST":
        form = PlacementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("q6")
    else:
        form = PlacementForm()
    students = Placement.objects.all()
    amazon = Placement.objects.filter(company_name__iexact="Amazon")
    return render(request, "q6/index.html", {"form": form, "students": students, "amazon": amazon})
