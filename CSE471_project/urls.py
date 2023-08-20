from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/farmer/', views.farmer_signup, name='farmer_signup'),
    path('signup/customer/', views.customer_signup, name='customer_signup'),
    path('signin/', views.signin, name='signin'),
    path('farmer/', views.farmer, name='farmer'),
    path("uploadvegetable",views.uploadvegetable,name="uploadvegetable"),
    path("product",views.Product,name="product"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('seller/', views.seller, name='seller'),
    path("payment", views.Payment, name="payment_gateway"),
    path("transport", views.Transport, name="transport"),
    path("checkout", views.checkout, name="checkout"),
    path('loan/', views.loan, name='loan'),
    path('investor/', views.investor, name='investor'),

]