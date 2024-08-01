from django.contrib import admin

# Register your models here.

from .models import*

admin.site.register(Contact_US)

admin.site.register(user)

admin.site.register(Add_product)

admin.site.register(Add_to_cart)

admin.site.register(Categories)

admin.site.register(Address)