# Generated by Django 5.0 on 2024-01-09 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0004_tbl_hospitaltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_consultancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultancy_name', models.CharField(max_length=50)),
                ('consultancy_email', models.CharField(max_length=50)),
                ('consultancy_head', models.CharField(max_length=50)),
                ('consultancy_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_address', models.CharField(max_length=50)),
                ('doctor_Contact', models.CharField(max_length=50)),
                ('doctor_gender', models.CharField(max_length=50)),
                ('doctor_email', models.CharField(max_length=50)),
                ('doctor_photo', models.FileField(upload_to='Hosdoc/')),
                ('doctor_proof', models.FileField(upload_to='Hosdoc/')),
                ('doctor_password', models.CharField(max_length=50)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_department')),
            ],
        ),
    ]
