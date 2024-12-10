from django import forms
from reservation.models import Booking


class Book_in(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date_in_fact']  # Только поле для редактирования даты заезда
        widgets = {
            'date_in_fact': forms.DateInput(attrs={'type': 'date'})
        }


class Book_out(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date_out_fact']  # Только поле для редактирования даты заезда
        widgets = {
            'date_out_fact': forms.DateInput(attrs={'type': 'date'})
        }

