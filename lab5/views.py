from django.shortcuts import render, redirect
from .forms import ExamStudentForm
from .models import ExamStudent

def index(request):
    if request.method == "POST":
        form = ExamStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("q5")
    else:
        form = ExamStudentForm()
    students = ExamStudent.objects.all()
    o_grade = ExamStudent.objects.filter(grade__iexact="O")
    return render(request, "q5_exam/index.html", {"form": form, "students": students, "o_grade": o_grade})
