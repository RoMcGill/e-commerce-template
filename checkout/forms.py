"""
imports
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    class to create form from model
    """
    class Meta:
        """
        meta to organise fields into specific order
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'country', 'postcode', 'town_or_city',
                  'street_address1', 'street_address2',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        add placeholders and classes, remove auto generated
        labels and set auto first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
             'full_name': 'Full Name',
             'email': 'Email Address',
             'phone_number': 'Phone Number',
             'country': 'Country',
             'postcode': 'Postal Code',
             'town_or_city': 'Town Or City',
             'street_address1': 'street Address 1',
             'street_address2': 'Street Address 2',
             'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
