from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем URL-адреса корзины
    path('cart/', include('cart.urls', namespace='cart')),
    # Подключаем URL-адреса каталога
    path('', include('catalog.urls')),
    # Подключаем URL-адреса заказов
    path('orders/', include('orders.urls', namespace='orders')),
]