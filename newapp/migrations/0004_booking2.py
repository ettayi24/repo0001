# Generated by Django 4.2.2 on 2023-07-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=25)),
                ('p_phone', models.CharField(max_length=30)),
                ('doc_name', models.CharField(max_length=30)),
                ('dep_name', models.CharField(max_length=30)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField()),
            ],
        ),
    ]
