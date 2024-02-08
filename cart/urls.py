from django.urls import path
from . import views
from .views import payment_view

urlpatterns = [

    path('add/', views.cart_add, name='cart_add'),
    path('payment/<int:product_id>/', views.payment_view, name='payment_view'),
    path('thank/', views.thanks, name='thanks'),
path('cart/', views.product_list, name='product_list'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

]