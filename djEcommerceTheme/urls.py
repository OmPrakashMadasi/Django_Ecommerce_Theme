
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from cart import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WebApp.urls')),
    path('cart/', include('cart.urls')),
    path('add/', views.cart_add, name='cart_add'),
path('payment/', views.payment_view, name='payment_view'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
