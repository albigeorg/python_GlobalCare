# Generated by Django 5.0 on 2023-12-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_hospitaltype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospitaltype', models.CharField(max_length=50)),
            ],
        ),
    ]
