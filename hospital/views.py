from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def aboutpage(request):
    return render(request,'about.html')
def Logout(request):
    logout(request)
    return redirect('loginpage')

def createaccountpage(request):
    user="none"
    error=""
    if(request.method=='POST'):
     name=request.POST['name']
     email=request.POST['email']
     password=request.POST['password']
     repeatpassword=request.POST['repeatpassword']
     gender=request.POST['gender']
     phonenumber=request.POST['phonenumber']
     address=request.POST['address']
     birthdate=request.POST['dateofbirth']
     bloodgroup=request.POST['bloodgroup']
    
    try:
     if password==repeatpassword:
      Patient.objects.create(name=name, email=email, gender=gender, phonenumber=phonenumber, address=address, birthdate=birthdate,bloodgroup=bloodgroup)
      user=User.objects.create_user(first_name=name, email=email,password=password,username=email) #admin willn't be able to see, as it is saved in user model
      pat_group=Group.objects.get(name='Patient')
      pat_group.user_set.add(user)
      user.save()
      error="no"
     else:
        error="yes"
    except Exception as e:
        error="yes"    
        d={'error':error}
    return render(request,'createaccount.html')
    
    

def loginpage(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				error = "no"
				login(request,user)
				
				g = request.user.groups.all()[0].name
				
				if g == 'Receptionist':
					page = "reception"
					d = {'error': error,'page':page}
					return render(request,'receptionhome.html',d)
				elif g == 'Patient':
					page = "patient"
					d = {'error': error,'page':page}
					return render(request,'patienthome.html',d)
			
		except Exception as e:
			print(e)
			
	return render(request,'login.html')

def doctorloginpage(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				error = "no"
				login(request,user)
				
				g = request.user.groups.all()[0].name
				if g == 'Doctor':
					page = "doctor"
					d = {'error': error,'page':page}
					return render(request,'doctorhome.html',d)
				
			
		except Exception as e:
			print(e)
			
	return render(request,'login.html')

def Home(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Doctor':
		return render(request,'doctorhome.html')
	elif g == 'Receptionist':
		return render(request,'receptionhome.html')
	elif g == 'Patient':
		return render(request,'patienthome.html')
         
"""def profile(request):
   if not request.user.is_active:
      return redirect('loginpage')
      
      g=request.user.groups.all()[0].name
      if g=='Patient':
         patient_details=Patient.objects.all().filter(email=request.user)
         d={'patient_details':patient_details}
         return render(request,'patientprofile.html',d)"""

def profile(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Patient':
		patient_detials = Patient.objects.all().filter(email=request.user)
		d = { 'patient_detials' : patient_detials }
		return render(request,'pateintprofile.html',d)
	elif g == 'Doctor':
		doctor_detials = Doctor.objects.all().filter(email=request.user)
		d = { 'doctor_detials' : doctor_detials }
		return render(request,'doctorprofile.html',d)
	
	

"""

def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	alldoctors = Doctor.objects.all()
	d = { 'alldoctors' : alldoctors }
	g = request.user.groups.all()[0].namedef MakeAppointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
    alldoctors = Doctor.objects.all()    
    d={'alldoctors':alldoctors}
    return """

def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	alldoctors = Doctor.objects.all()
	d = { 'alldoctors' : alldoctors }
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		if request.method == 'POST':
			doctoremail = request.POST['doctoremail']
			doctorname = request.POST['doctorname']
			patientname = request.POST['patientname']
			patientemail = request.POST['patientemail']
			appointmentdate = request.POST['appointmentdate']
			appointmenttime = request.POST['appointmenttime']
			symptoms = request.POST['symptoms']
			try:
				Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,patientname=patientname,patientemail=patientemail,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescription="")
				error = "no"
			except:
				error = "yes"
			e = {"error":error}
			return render(request,'patientmakeappointments.html',e)
		elif request.method == 'GET':
			return render(request,'patientmakeappointments.html',d)
                
def viewappointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
	#print(request.user)
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		upcomming_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		#print("Upcomming Appointment",upcomming_appointments)
		previous_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(patientemail=request.user,status=False).order_by('-appointmentdate')
		#print("Previous Appointment",previous_appointments)
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'patientviewappointments.html',d)
	elif g == 'Doctor':
		if request.method == 'POST':
			prescriptiondata = request.POST['prescription']
			idvalue = request.POST['idofappointment']
			Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,status=False)
			#print(idvalue)
			#print(pname)
			#p = {"idvalue":idvalue,"pname":pname}
			#return render(request,'doctoraddprescription.html',p)
		upcomming_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		#print("Upcomming Appointment",upcomming_appointments)
		previous_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=request.user,status=False).order_by('-appointmentdate')
		#print("Previous Appointment",previous_appointments)
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'doctorviewappointment.html',d)