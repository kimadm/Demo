from django.urls import path
from . import views

urlpatterns = [
    # --- Старые, рабочие URL-адреса ---
    path('', views.index, name='index'),
    path('components/', views.components_page, name='components'),
    path('components/category/<int:category_id>/', views.components_page, name='components_by_category'),

    # Строка будет отвечать за страницы отдельных товаров
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
