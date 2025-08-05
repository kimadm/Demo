from django import forms

# Создаем список выбора от 1 до 20
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # Поле для выбора количества с выпадающим списком
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int, # Преобразуем значение в целое число
        label='Количество',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # Скрытое поле, которое говорит, нужно ли перезаписать количество или добавить к существующему
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
