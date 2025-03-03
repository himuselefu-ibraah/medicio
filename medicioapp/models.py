from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    hiredate = models.DateField()

    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.lastname

class Ward(models.Model):
    name = models.CharField(max_length=100)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateTimeField()
    department = models.CharField(max_length=50)
    doctor =models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name







