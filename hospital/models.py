from django.db import models

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Doctor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)
	specialization = models.CharField(max_length=50)
 
def __str__(self):
      return self.name

class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	doctoremail = models.EmailField(max_length=50)
	patientname = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	appointmenttime = models.TimeField(max_length=10)
	symptoms = models.CharField(max_length=100)
	prescription = models.CharField(max_length=200)
	status = models.BooleanField()
	
	
def __str__(self):
    return self.patientname+ "you have an appointment with "+ self.doctorname + " on "+self.appointmentdate
      
      
