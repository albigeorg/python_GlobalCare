from django.db import models
from User.models import *

# Create your models here.

class  tbl_updatemedicine(models.Model):
   updatemedicine_report=models.FileField(upload_to='HosDOc/')
   updatemedicine_medical=models.CharField(max_length=50)
   updatemedicine_major=models.CharField(max_length=50)
   appointment=models.ForeignKey(tbl_appointment,on_delete=models.CASCADE,null=True)


class tbl_prescribtion(models.Model):
   prescribtion_medicine=models.CharField(max_length=50)
   prescribtion_diet=models.CharField(max_length=50)
   appointment=models.ForeignKey(tbl_appointment,on_delete=models.CASCADE,null=True)
   