from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.


class tbl_consultancy(models.Model):
    consultancy_name=models.CharField(max_length=50)
    consultancy_email=models.CharField(max_length=50)
    consultancy_head=models.CharField(max_length=50)
    consultancy_password=models.CharField(max_length=50)
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE,null=True)


class tbl_doctor(models.Model):
    doctor_name=models.CharField(max_length=50)
    doctor_address=models.CharField(max_length=50)
    doctor_Contact=models.CharField(max_length=50)
    doctor_gender=models.CharField(max_length=50)
    doctor_email=models.CharField(max_length=50)
    Department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    doctor_photo=models.FileField(upload_to='HosDoc/')
    doctor_proof=models.FileField(upload_to='HosDoc/')
    doctor_password=models.CharField(max_length=50)
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE,null=True)

class tbl_gallery(models.Model):
    gallery_pic=models.FileField(upload_to='HosDoc/')
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE,null=True)





