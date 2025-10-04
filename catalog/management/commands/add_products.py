from decimal import Decimal

from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавление тестовых продуктов в базу данных с предварительной очисткой.'

    def handle(self, *args, **kwargs):
        try:
            Product.objects.all().delete()
            Category.objects.all().delete()
        except Exception as e:
            print(e)

        category, _ = Category.objects.get_or_create(category_name='детская литература',
                                                  category_description='художественная литература для детей')

        products = [
            {'product_name': 'Гарри Поттер и философский камень',
             'product_description': 'Д. Роулинг Культовая классика детской литературы', 'category': category,
             'price': Decimal(1200)},
            {'product_name': 'Гарри Поттер и Тайная комната',
             'product_description': 'Д. Роулинг Культовая классика детской литературы', 'category': category,
             'price': Decimal(1300)},
        ]
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт {product.product_name} добавлен.'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт {product.product_name} НЕ добавлен.'))
