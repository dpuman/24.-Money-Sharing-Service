from django.contrib import admin
from .models import Customer, Account, Transection
# Register your models here.

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transection)
