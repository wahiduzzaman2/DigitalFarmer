from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Item,Loan
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        x=User.objects.create_user(username=username,email=email,password=password)
        x.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'sign_up.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            return render(request,'home.html')
        else:
            messages.info(request,'Username OR password is incorrect')
    else:
        return render(request, 'login.html')
def contact(request):
    return render(request,'contact.html')

def farmers(request):
    items=Item.objects.all()
    return render(request,'farmers.html',{'items':items})

def farmers_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                return redirect('farmers')
            else:
                messages.error(request, 'This account is not active.')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'farmers_signin.html')

def farmers_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        x = User.objects.create_user(username=username, email=email, password=password)
        x.save()
        print('user created')
        return render(request, 'farmers_signup.html')
    else:
        return render(request, 'sign_up.html')
# def logout_view(request):
#     logout(request)
#     return redirect('home')

from .forms import VegetableForm,Loanform

def upload_vegetable(request):
    if request.method == 'POST':
        form = VegetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farmers')  # Replace 'homepage' with the URL name of your farmers portal homepage
    else:
        form = VegetableForm()

    return render(request, 'upload_vegetable.html', {'form': form})

def seeds(request):
    return render(request,'seeds.html')
def loan(request):
    if request.method == 'POST':
        form = Loanform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    else:
        form = Loanform()

    return render(request, 'loan.html', {'form': form})