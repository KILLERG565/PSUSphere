from django import forms
from .models import Item  # Replace with your actual model

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']  # Replace with your model fields