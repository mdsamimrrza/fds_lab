from django.shortcuts import render, redirect
from .forms import GradeStudentForm, UpdateGradeForm
from .models import GradeStudent


def index(request):
    add_form = GradeStudentForm()
    update_form = UpdateGradeForm()
    if request.method == "POST":
        if "add_student" in request.POST:
            add_form = GradeStudentForm(request.POST)
            if add_form.is_valid():
                add_form.save()
                return redirect("q8")
        if "update_grade" in request.POST:
            update_form = UpdateGradeForm(request.POST)
            if update_form.is_valid():
                name = update_form.cleaned_data["name"]
                new_grade = update_form.cleaned_data["new_grade"]
                GradeStudent.objects.filter(
                    name__iexact=name).update(grade=new_grade)
                return redirect("q8")
    students = GradeStudent.objects.all()
    context = {"add_form": add_form,
               "update_form": update_form, "students": students}
    return render(request, "q8/index.html", context)
