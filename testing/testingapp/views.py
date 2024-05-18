from django.shortcuts import render
from django.http import HttpResponse
from testingapp.models import Students
from testingapp.forms import studentform
from testingapp.forms import getdetails
from testingapp.forms import updatedetails
from testingapp.forms import deleteform
def student(request,r):
    try:
        sroll = Students.objects.get(roll=r)
    except:
        return HttpResponse(f"{r} not found")
    return HttpResponse(sroll.name)
def about(request):
    return render(request,"about.html")
def index(request):
    return render(request,"index.html")

def create(request):
    if (request.method=="POST"):
        form = studentform(request.POST)
        if(form.is_valid()):
            student_id = form.cleaned_data['id']
            student_name = form.cleaned_data['name']
            db = Students.objects.create(roll=student_id,name=student_name)
            db.save()
            return HttpResponse("created")
            
    form = studentform()
    return render(request,"create.html",{"form":form})
def read(request):
    if(request.method=="POST"):
        form = getdetails(request.POST)
        if(form.is_valid()):
            stud_id = form.cleaned_data["id"]
            readobj = Students.objects.get(roll=stud_id)
            return render(request,"read.html",{"student":readobj})
        
    formg = getdetails()
    return render(request,"read.html",{"form":formg})

def update(request):
    if(request.method=="POST"):
        form = updatedetails(request.POST)
        if(form.is_valid()):
            stud_id = form.cleaned_data["id"]
            stud_name = form.cleaned_data["name"]
            obj = Students.objects.filter(roll=stud_id).update(name=stud_name)
            return HttpResponse(f"{stud_name} is updated for roll no{stud_id}")
        
    formu = updatedetails()
    return render(request,"update.html",{"form":formu})

def delete(request):
    if(request.method=="POST"):
        form = deleteform(request.POST)
        if(form.is_valid()):
            stud_id = form.cleaned_data["id"]
            try:
                stud = Students.objects.get(roll=stud_id)
                stud.delete()
            except:
                return HttpResponse(f"Details for {stud_id} not found")
            return HttpResponse(f"{stud.name} is deleted Successfully")
        
    formd = deleteform()
    return render(request,"delete.html",{"form":formd})
            