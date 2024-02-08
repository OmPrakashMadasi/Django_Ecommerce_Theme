from django import forms
from .models import Payment
from django.core import validators

import datetime



class PaymentForm(forms.ModelForm):
        class Meta:
                model = Payment
                fields = ['card_number', 'expiration_date', 'cvv', 'amount']

                def __init__(self, *args, **kwargs):
                        super(PaymentForm, self).__init__(*args, **kwargs)
                        self.fields['card_number'].widget.attrs.update({'placeholder': 'Card Number'})
                        self.fields['expiration_date'].widget.attrs.update({'placeholder': 'Expiration Date'})
                        self.fields['cvv'].widget.attrs.update({'placeholder': 'CVV'})
                        self.fields['amount'].widget.attrs.update({'placeholder': 'Amount'})
                #     self.fields['timestamp'].widget.attrs.update({'placeholder': ''})