# Generated by Django 4.2.2 on 2023-07-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0014_alter_booking_booked_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='PLACE',
            new_name='PASSWORD',
        ),
    ]
