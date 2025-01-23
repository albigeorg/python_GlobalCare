from django.db import models
from Hospital.models import *

# Create your models here.
class  tbl_available(models.Model):
   available_date=models.DateField(max_length=50)
   available_formtime=models.CharField(max_length=50)
   available_totime=models.CharField(max_length=50)
   Doctor=models.ForeignKey(tbl_doctor,on_delete=models.CASCADE,null=True)


class  tbl_slots(models.Model):
   slots=models.CharField(max_length=50)
   available=models.ForeignKey(tbl_available,on_delete=models.CASCADE,null=True)
   slot_status=models.CharField(max_length=2,default=0)
