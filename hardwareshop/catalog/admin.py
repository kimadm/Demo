from django.contrib import admin
from .models import Product, Category # Убедится, что Category здесь импортирована

# Регистрируем обе модели
admin.site.register(Product)
admin.site.register(Category)