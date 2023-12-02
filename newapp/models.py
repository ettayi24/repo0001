from django.db import models

import datetime,random
i=random.randrange(9)

def randomdate(i):
    basedate = datetime.datetime(2023, 8, 31, 10, 00, 00)
    delta = datetime.timedelta(days=i, hours=i)
    date=basedate+delta
    return date





# Create your models here.
class Department(models.Model): 
    dep_name=models.CharField(max_length=25)
    description=models.TextField(max_length=200)
     
    def __str__(self):
        return self.dep_name 
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=20)
    doc_spec=models.CharField(max_length=100)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.FileField()

    def __str__(self):
        return self.doc_name +' ' + '(' + self.doc_spec + ')'
    
    
    
class Booking(models.Model):
    p_name=models.CharField(max_length=25)
    p_phone=models.CharField(max_length=30)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    booked_on=models.DateField(auto_now=True)
    booked_to=models.DateTimeField(null=True)
#convert  usename to lowercase
    def save(self, *args, **kwargs):
      self.p_name = self.p_name.lower()
    #   self.booked_to=randomdate(i)
      return super(Booking, self).save(*args, **kwargs)

#temporarily created to check save
class Booking2(models.Model):
    p_name=models.CharField(max_length=25)
    p_phone=models.CharField(max_length=30)
    doc_name=models.CharField(max_length=30)
    dep_name=models.CharField(max_length=30)
    booked_on=models.DateField(auto_now=True)
    booked_to=models.DateTimeField(null=True)

# model to check foreifn key working
class Sample(models.Model):
    NAME=models.ForeignKey(Doctors,on_delete=models.CASCADE,related_name='pappu')
    SPEC=models.ForeignKey(Doctors,on_delete=models.CASCADE,related_name='pinki')
    DEP=models.ForeignKey(Department,on_delete=models.CASCADE)

#user register
class Register(models.Model):
    NAME=models.CharField(max_length=30)
    PASSWORD=models.CharField(max_length=30)
    EMAILID=models.EmailField()





