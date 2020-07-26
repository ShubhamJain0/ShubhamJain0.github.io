from django.contrib import admin
from mainapp import models
# Register your models here.

admin.site.register(models.CustomUserModel)
admin.site.register(models.orderfood)
admin.site.register(models.yourorder)
admin.site.register(models.manageaddress)
admin.site.register(models.cartitems)
admin.site.register(models.Order)
admin.site.register(models.Image)
admin.site.register(models.BookingTable)