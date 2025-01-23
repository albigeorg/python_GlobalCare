from django.db import models
from Guest.models import *
from Consultancy.models import *

# Create your models here.

class  tbl_complaint(models.Model):
   complaint_title=models.CharField(max_length=50)
   complaint_com=models.CharField(max_length=50)
   complaint_reply = models.CharField(max_length=50)
   complaint_date = models.DateField(auto_now_add=True) 
   user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
   hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE,null=True)
   consultancy=models.ForeignKey(tbl_consultancy,on_delete=models.CASCADE,null=True)
   complaint_status=models.CharField(max_length=10,default=0)
   doctor=models.ForeignKey(tbl_doctor,on_delete=models.CASCADE,null=True)



class tbl_feedback(models.Model):
   feedback_title=models.CharField(max_length=50)
   feedback_date=models.DateField(auto_now_add=True) 
   user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
   hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE,null=True)
   consultancy=models.ForeignKey(tbl_consultancy,on_delete=models.CASCADE,null=True)
   doctor=models.ForeignKey(tbl_doctor,on_delete=models.CASCADE,null=True)


class tbl_appointment(models.Model):
   appointment_date=models.DateField(auto_now_add=True)
   appointment_status=models.CharField(max_length=2,default=0)
   slot=models.ForeignKey(tbl_slots,on_delete=models.CASCADE,null=True)
   user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)


   
