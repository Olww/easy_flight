from django.forms import ModelForm
from django import forms
from tickets.models import Tickets
class SearchForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('tickets_from', 'tickets_to', 'tickets_date',)
        widgets = {
            'tickets_from':forms.TextInput(
                attrs={'id': 'tickets-from','placeholder':'From'}
            ),
            'tickets_to':forms.TextInput(
                attrs={'id': 'tickets-to','placeholder':'To'}
            ),
            'tickets_date':forms.DateInput(
                attrs={'id': 'tickets-date', 'placeholder':'00.00.0000'}
            ),
        }
