from django.shortcuts import render, redirect
from .forms import boidataForm
from .models import biodata


def index(request):
    if request.method == "POST":
        form = boidataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = boidataForm()
    people = biodata.objects.all()
    return render(request, "lab1/index.html", {"form": form, "people": people})
