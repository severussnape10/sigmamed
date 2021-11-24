from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
genders =[('Male','Male'),('Female','Female'),('Other','Other'),('Not specified','Not specified')]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=genders,default='Not specified')
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Emergency Medicine Specialists')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    location = models.CharField(max_length=40,null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.name,self.location)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=genders,default='Not specified')
    mobile = models.CharField(max_length=20,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    hospitalId = models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    hospitalName = models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)

