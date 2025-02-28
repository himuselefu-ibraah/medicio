from django.shortcuts import render,redirect
from medicioapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def service(request):
    return render(request,'service-details.html')
def starter(request):
    return render(request,'starter-page.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def doctor(request):
    return render(request,'Doctor.html')
def department(request):
    return render(request,'department.html')
def appoint(request):
    if request.method == "POST":
        myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
        myappointments.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment form.html')

