# Generated by Django 4.2.2 on 2023-07-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0012_booking_booked_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking2',
            name='booked_to',
            field=models.DateTimeField(null=True),
        ),
    ]
