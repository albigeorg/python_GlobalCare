# Generated by Django 5.0 on 2024-01-18 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consultancy', '0003_tbl_slots_available_tbl_slots_slot_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_available',
            old_name='doctor',
            new_name='Doctor',
        ),
    ]
