# Generated by Django 5.0 on 2024-02-05 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_tbl_consultancy_hospital_tbl_doctor_hospital'),
        ('User', '0011_tbl_feedback_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_complaint',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.tbl_doctor'),
        ),
    ]
