from django.shortcuts import render

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
    return render(request,'appointment form.html')
