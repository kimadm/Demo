from django.contrib import admin
from django.urls import path, include # Добавьте 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), # Эта строка перенаправит все на ваше приложение
]