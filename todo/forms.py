from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Tell the form which model it is associated with
    class Meta:
        model = Item
        # Which fields to display from the model
        fields = ['name', 'is_done']
