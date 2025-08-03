from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем URL-адреса корзины здесь
    path('cart/', include('cart.urls', namespace='cart')),

    # Подключаем URL-адреса каталога
    path('', include('catalog.urls')),
]
