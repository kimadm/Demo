from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# --- Ваши существующие, рабочие функции ---
def index(request):
    products = Product.objects.all()[:4]
    context = {'products': products}
    return render(request, 'index.html', context)

def components_page(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        current_category = category
    else:
        products = Product.objects.all()
        current_category = None
    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'komplektuyushchiye.html', context)

# --- Убедитесь, что эта функция выглядит именно так ---
def product_detail(request, product_id):
    # Эта функция находит товар по ID и передает его в HTML-шаблон
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
