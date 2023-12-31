from django.shortcuts import render
from django.contrib.auth.models import User
from pyexpat.errors import messages
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import FarmerSignupForm, CustomerSignupForm, SigninForm,vegetableform,billingform,Loanform
from .models import Items,Loan,billing
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

def index(request):
    return render(request,'index.html')

def farmer_signup(request):
    if request.method == 'POST':
        form = FarmerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_farmer = True
            user.save()
            login(request, user)
            return redirect('/')  # Replace 'home' with your desired destination after successful signup
    else:
        form = FarmerSignupForm()
    return render(request, 'farmer_signup.html', {'form': form})

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_seller= True
            user.save()
            login(request, user)
            return redirect('/')  # Replace 'home' with your desired destination after successful signup
    else:
        form = CustomerSignupForm()
    return render(request, 'customer_signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_farmer:
                    return render(request,"farmer.html")
                else:
                    if user.is_seller:
                         return render(request,"seller.html")
                    else:
                        return render(request,'index.html')
                #return redirect('signup/customer/')  # Replace 'home' with your desired destination after successful login
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})

@login_required(login_url='signin')
def farmer(request):
    return render(request,'farmer.html')


def uploadvegetable(request):
    if request.method=='POST':
        form=vegetableform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'product.html')
    else:
        form=vegetableform()
    return render(request,'uploadvegetale.html',{'form':form})

def Product(request):
    items = Items.objects.all()
    return render(request, 'product.html', {'items': items})


@login_required(login_url="signin")
def cart_add(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="signin")
def item_clear(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="signin")
def item_increment(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="signin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="signin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="signin")
def cart_detail(request):
    return render(request, 'cart/cart.html')



@login_required(login_url="signin")
def seller(request):
    return render(request,'seller.html')

def Payment(request):
    return render(request,'Payment/payment_gateway.html')
def Transport(request):
    return render(request,'Transport/index.html')
def checkout(request):
    temp = billingform()
    if request.method=='POST':
        temp=billingform(request.POST,request.FILES)
        if temp.is_valid():
            temp.save()
            return render(request,'Payment/payment_gateway.html')
        else:
            temp=billingform()
    return render(request,'checkout.html',{'form':temp})



def loan(request):
    if request.method == 'POST':
        form = Loanform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = Loanform()

    return render(request, 'loan.html', {'form': form})

def investor(request):
    req = Loan.objects.all()
    return render(request, 'investor.html', {'req': req})

