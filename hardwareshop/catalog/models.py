from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image_url = models.URLField(max_length=200, verbose_name="URL изображения")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

    def __str__(self):
        return self.name

class ShopContact(models.Model):
    name = models.CharField("Название магазина", max_length=100, default="IT365 Shop")
    address = models.TextField("Адрес")
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")
    working_hours = models.CharField("Часы работы", max_length=100)
    latitude = models.FloatField("Широта", default=43.232290)
    longitude = models.FloatField("Долгота", default=76.948528)

    class Meta:
        verbose_name = "Контакт магазина"
        verbose_name_plural = "Контакты магазина"

    def __str__(self):
        return self.name