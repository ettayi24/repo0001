from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)


#To display Booking class in tabular format in admin page we create this class and register with the relavant class
class Bookingadmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','dep_name','doc_name','booked_on','booked_to')
admin.site.register(Booking2,Bookingadmin)
admin.site.register(Sample)
admin.site.register(Booking)
admin.site.register(Register)