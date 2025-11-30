from django.shortcuts import render, redirect
from  .forms import studentForms
from .models import studentCIE

# Create your views here.
def index( request):
    if request.method == "POST":
        form = studentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = studentCIE()
    students = studentCIE.objects.all()
    low_cie = studentCIE.objects.filter(cie_marks__lt=20)
    context = {"form":form,"students": students , "low_cie": low_cie}
    return render(request , "q2/index.html",context)
        

