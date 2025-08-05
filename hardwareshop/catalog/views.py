from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ShopContact
from cart.forms import CartAddProductForm # Импортируем форму

def index(request):
    products = Product.objects.all()[:4]
    return render(request, 'index.html', {'products': products})

def components_page(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    current_category = get_object_or_404(Category, id=category_id) if category_id else None
    return render(request, 'komplektuyushchiye.html', {
        'products': products,
        'categories': categories,
        'current_category': current_category
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Создаем и передаем форму для добавления в корзину
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {
        'product': product,
        'cart_product_form': cart_product_form
    })

def contact_page(request):
    contact = ShopContact.objects.first()
    if not contact:
        contact = ShopContact.objects.create(
            address="г. Алматы, проспект Назарбаева, 223",
            phone="+7 (775) 996-00-64",
            email="shop@it365.com",
            working_hours="Пн-Пт с 10:00 до 19:00"
        )
    return render(request, 'contacts.html', {'contact': contact})
