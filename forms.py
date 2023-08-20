from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Items,Billing,Loan

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



class Loanform(forms.ModelForm):
    class Meta:
        model = Loan
        fields= ['name','email','sop','ask_amount']

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['name', 'phone', 'email', 'address', 'city', 'zip_code']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.transport_cost = instance.calculate_transport_cost()
        if commit:
            instance.save()
        return instance