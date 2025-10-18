import os

from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
MAX_IMAGE_SIZE = 5 * 1024 * 1024
ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'image','category', 'price', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['is_active'].widget.attrs.update({
            'class': 'form-check-input'
        })


    def clean_product_name(self):
        cleaned_data = super(ProductForm, self).clean()
        product_name = cleaned_data.get('product_name').lower()
        for word in FORBIDDEN_WORDS:
            if word in product_name:
                raise ValidationError(f"Запрещено использовать слова в названии: {', '.join(FORBIDDEN_WORDS)}")
        return product_name

    def clean_product_description(self):
        cleaned_data = super(ProductForm, self).clean()
        product_description = cleaned_data.get('product_description').lower()
        for word in FORBIDDEN_WORDS:
            if word in product_description:
                raise ValidationError(f"Запрещено использовать слова в описании: {', '.join(FORBIDDEN_WORDS)}")
        return product_description


    def clean_price(self):
        cleaned_data = super(ProductForm, self).clean()
        price = cleaned_data.get('price')
        if price:
            price = float(price)
            if price < 0:
                raise ValidationError("Цена не может быть отрицательной!")
        return price

    def clean_image(self):
        cleaned_data = super(ProductForm, self).clean()
        image = cleaned_data.get('image')
        if image:
            image_format = os.path.splitext(image.name)[1].lower()
            if image_format not in ALLOWED_IMAGE_EXTENSIONS:
                raise ValidationError("Разрешены только файлы в формате JPEG или PNG")
            if image.size > MAX_IMAGE_SIZE:
                raise ValidationError(f"Размер файла не должен превышать 5 МБ")
        return image
