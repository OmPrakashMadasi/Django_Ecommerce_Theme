from django.shortcuts import render, redirect
from .models import Product
from .forms import PaymentForm
from .models import CartItem
from . import forms
def cart_add(request):
    products = Product.objects.all()
    return render(request, 'cart_add.html',{'products': products})
def product_list(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart_checkout.html', {'cart_items': cart_items, 'total_price': total_price})
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('product_list')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('product_list')


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')

