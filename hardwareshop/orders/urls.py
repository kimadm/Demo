from django.urls import path
from . import views

# app_name нужен, чтобы Django мог различать URL-имена в разных приложениях
app_name = 'orders'

urlpatterns = [
    # Оставить только один маршрут для создания заказа
    path('create/', views.order_create, name='order_create'),
]
