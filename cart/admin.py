from django.contrib import admin
from .models import Category, Product, CartItem, Payment
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('card_number','expiration_date','cvv','amount',)

admin.site.register(Payment, PaymentAdmin)