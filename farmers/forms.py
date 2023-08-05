from django import forms
from .models import Item,Loan

class VegetableForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'picture']
class Loanform(forms.ModelForm):
    class Meta:
        model = Loan
        fields= ['name','email','sop','ask_amount']
