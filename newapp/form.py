from django import forms

from .models import Booking

#for date picker
class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields=('p_name','p_phone','doc_name','dep_name')

        widgets={
        }

        labels={
            'p_name':'PATIENT NAME',
            'p_phone':'CONTACT NUMBER',
            'doc_name':'DOCTORS NAME ',
            'dep_name':'DEPARTMENT NAME',
        }