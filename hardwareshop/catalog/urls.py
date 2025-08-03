from django.urls import path
from . import views

urlpatterns = [
    # --- Ваши существующие URL-адреса ---
    path('', views.index, name='index'),
    path('components/', views.components_page, name='components'),
    path('components/category/<int:category_id>/', views.components_page, name='components_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contact_page, name='contacts'),
]
