from django.shortcuts import render,HttpResponse
from datetime import date
from .models import *
from .form import BookingForm
from django.db.models import Count
#to generate random time and data
import datetime,random
i=random.randrange(9)

def randomdate(i):
    basedate = datetime.datetime(2023, 12, 31, 10, 00, 00)
    delta = datetime.timedelta(days=i, hours=i)
    date=basedate+delta
    return date





# Create your views here.
def home(request):
    return render(request,'base.html')
def department(request):
    data=Department.objects.all()
    return render(request,'department.html',{'result':data})
def doctors(request):
    data=Doctors.objects.all()
    return render(request,'doctors.html',{'result':data})

#to reach to booking through doctors cards
def booking(request):
    id=request.POST['id']
    data=Doctors.objects.get(id=id)
    return render(request,'booking.html',{'result':data})

# to reach booking directly
def book(request):
    if request.method=='POST':
        # p_name=request.POST['p_name']
        # p_phone=request.POST['p_phone']
        # doc_name=request.POST['doc_name.doc_name']
        # department=request.POST['dep_name.dep_name']
        # form=Booking(booked_to=date,p_name=p_name,p_phone=p_phone,doc_name=doc_name,dep_name=department)
        form=BookingForm(request.POST)
        if form.is_valid():
                form.save()
                # print(randomdate)
                obj=Booking.objects.filter(p_name=request.POST['p_name'],doc_name=request.POST['doc_name']).update(booked_to=randomdate(i))
                return render(request,'confirmation.html')
    form=BookingForm()
    return render(request,'booking2.html',{'result':form})

#to save enterted data to booking database
def savebooking(request):
    p_name=str(request.POST['pname']).lower()
    mobile=request.POST['mobile']
    doc_name=request.POST['doc_name']
    dep_name=request.POST['dep_name']
    # booking_date=request.POST['booking_date']
    booking_date=randomdate(i)
    today=date.today()
    data=Booking2(p_name=p_name,p_phone=mobile,doc_name=doc_name,dep_name=dep_name,booked_to=booking_date,booked_on=today)
    data.save()
    return render(request,'confirmation.html')

def contactpage(request):
     return render(request,'contactpage.html')

def aboutpage(request):
     return render(request,'aboutpage.html')

#to get register page
def toRegister(request):
     if request.method=='POST':
          username=str(request.POST['username']).lower()
          password=request.POST['password']
          email=request.POST['email']
          n=Register.objects.filter(NAME=username,EMAILID=email).count()
          if n==0:
              obj=Register(NAME=username,PASSWORD=password,EMAILID=email)
              obj.save()
              return render(request,'base.html')
          else:return render(request,'registeralert.html')
     return render(request,'register.html')

#to get log-in page
def toLogin(request):
     if request.method=='POST':
          username=str(request.POST['username']).lower()
          password=request.POST['password']
          try:
              data=Register.objects.get(NAME=username,PASSWORD=password)
              newdata1=Booking.objects.filter(p_name=username)
              newdata2=Booking2.objects.filter(p_name=username)
              return render(request,'myaccount.html',{'data':newdata1,'profile':data,'data2':newdata2})
          except Register.DoesNotExist:
               return render(request,'register.html')
               
     return render(request,'login.html')

#adminpage access
def adminpage(request):
          data1=Booking.objects.all().order_by('p_name')
          data2=Booking2.objects.all().order_by('p_name')
          return render(request,'adminpage.html',{'result1':data1,'result2':data2})
      
         
def success(request):
    return render(request,'confirmation.html')
          