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
        return redirect('/show')
    else:
        return render(request,'appointment form.html')

def contact(request):
    if request.method == "POST":
        myform = Address(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']

        )
        myform.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')

def show(request):
    all = Appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
    deleteappointments=Appointment.objects.get(id=id)
    deleteappointments.delete()
    return redirect('/show')
