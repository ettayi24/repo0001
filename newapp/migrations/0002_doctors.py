# Generated by Django 4.2.2 on 2023-07-02 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=20)),
                ('doc_spec', models.CharField(max_length=100)),
                ('doc_image', models.FileField(upload_to='')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.department')),
            ],
        ),
    ]
