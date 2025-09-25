from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name']


class ContactInfo(models.Model):
    country = models.CharField(max_length=100, verbose_name='страна')
    inn = models.CharField(max_length=20, unique=True, verbose_name='ИНН')
    address = models.CharField(max_length=255, verbose_name='адрес')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    email = models.EmailField(unique=True, verbose_name='email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f"{self.country}, {self.address}, {self.phone}, {self.email}"

    class Meta:
        verbose_name = 'контактная информация'
        verbose_name_plural = 'контактные данные'
