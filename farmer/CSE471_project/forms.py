from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Items,billing,Loan

class FarmerSignupForm(UserCreationForm):
    # Add any additional fields for farmer signup
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class CustomerSignupForm(UserCreationForm):
    # Add any additional fields for customer signup
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class SigninForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class vegetableform(forms.ModelForm):
    class Meta:
        model=Items
        fields=['name','payment','price','total','available','picture']

class billingform(forms.ModelForm):
    class Meta:
        model=billing
        fields=['name','phone','email','address','city','zip_code']

class Loanform(forms.ModelForm):
    class Meta:
        model = Loan
        fields= ['name','email','sop','ask_amount']