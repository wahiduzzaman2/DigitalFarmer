from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Items)
admin.site.register(billing)
admin.site.register(Loan)