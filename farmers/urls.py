from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/',views.contact,name='contact'),
    path('farmers_signin/farmers/',views.farmers,name='farmers'),
    path('farmers_signin/',views.farmers_signin,name='farmers_signin'),
    path('farmers_signup/',views.farmers_signup,name='farmers_signup'),
    path('farmers_signin/farmers/upload_vegetable/',views.upload_vegetable,name='upload_vegetable'),
    path('farmers_signin/farmers/seeds/',views.seeds,name='seeds'),
    path('farmers_signin/farmers/loan/',views.loan,name='loan'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


