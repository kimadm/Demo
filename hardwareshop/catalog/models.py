from django.db import models


# Сначала определяем класс Категории
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name


# Теперь определяем класс Товара, который использует Категорию
class Product(models.Model):
    # Добавляем null=True и blank=True, чтобы разрешить полю быть пустым.
    # Это нужно для существующих товаров в базе данных.
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
