# Generated by Django 5.0.2 on 2024-02-23 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_remove_tbl_place_district_delete_tbl_district_and_more'),
        ('Guest', '0005_remove_tbl_newhospital_hospitaltype_delete_tbl_user_and_more'),
        ('Hospital', '0007_remove_tbl_doctor_department_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_admin',
        ),
        migrations.DeleteModel(
            name='tbl_department',
        ),
        migrations.DeleteModel(
            name='tbl_hospitaltype',
        ),
    ]
