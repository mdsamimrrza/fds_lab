from django.shortcuts import render, redirect
from .models import examfeemodel
from .forms import examfeeforms


def index(request):
    if request.method == "POST":
        # delete unpaid students
        if "delete_unpaid" in request.POST:
            examfeemodel.objects.filter(exam_fee=0).delete()
            return redirect("index")

        # add student fee record
        form = examfeeforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = examfeeforms()

    students = examfeemodel.objects.all()
    return render(request, "q3/index.html", {"form": form, "students": students})
