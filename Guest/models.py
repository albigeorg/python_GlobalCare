from django.db import models
from Admin.models import *

# Create your models here.


class tbl_newhospital(models.Model):
    hospital_name=models.CharField(max_length=50)
    hospital_email=models.CharField(max_length=50)
    hospital_contact=models.CharField(max_length=50)
    hospital_address=models.CharField(max_length=50)
    hospital_logo=models.FileField(upload_to='HosDoc/')
    hospital_proof=models.FileField(upload_to='HosDOc/')
    hospital_password=models.CharField(max_length=50)
    hospital_vstatus=models.CharField(max_length=2,default=0)
    hospitaltype=models.ForeignKey(tbl_hospitaltype,on_delete=models.CASCADE)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)


class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='userdoc/')
    user_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)