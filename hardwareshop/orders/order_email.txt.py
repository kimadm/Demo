Здравствуйте, {{ order.first_name }} {{ order.last_name }}!

Благодарим вас за заказ #{{ order.id }} в IT365 Shop.

Детали заказа:
{% for item in items %}
- {{ item.product.name }}: {{ item.quantity }} x {{ item.price }} ₸
{% endfor %}

Общая сумма: {{ order.get_total_cost }} ₸

Адрес доставки: {{ order.postal_code }}, {{ order.city }}, {{ order.address }}

С уважением,
Команда IT365 Shop