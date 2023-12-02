# Generated by Django 4.2.2 on 2023-07-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=30)),
                ('PLACE', models.CharField(max_length=30)),
                ('EMAILID', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_on',
            field=models.DateField(auto_now=True),
        ),
    ]