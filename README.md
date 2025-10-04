# Интернет-магазин.
## Описание:
_Я создаю проект интернет-магазина, который буду дорабатывать на каждом уроке в течение всего курса.
В уроке "Работа с ORM в Django" было выполнено подключение PostgreSQL к проекту, созданы две модели
Product и Category, которые были перенесены в БД (созданную в pgAdmin 4) с помощью миграций;
зарегистрированы и настроены модели в админке, также наполнена БД через Django shell,
созданы фикстуры для моделей и реализована кастомная команда для добавления тестовых данных._

## Установка:
Клонируйте репозиторий:
```
git clone https://github.com/Andrievskis/Lesson_22.git

```
Установите зависимости:
```
pip install -r requirements.txt

```
## Использование:
На данный момент проект работает локально. 
Можно обращаться по двум эндпоинтам: "/"(главная) и "contacts" (контакты).
Также при заполнении данных на станице "contacts" будет получено сообщение:
```
Спасибо, Анна! Ваше сообщение: + 70000000000 получено.
```
Необходимо создать базу данных в ручном режиме (pgAdmin 4):
```
CREATE DATABASE <имя вашей базы данных>;
```
Внести изменения в settings.py
В приложении каталога создайте модели Product, Category, ContactInfo и опишите для них базовые настройки.
Выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```
Создайте суперпользователя.
```
python manage.py createsuperuser
```
Зарегистрируйте и настройте отображение моделей Product, Category, ContactInfo в [admin.py](catalog/admin.py)

Через инструмент shell заполните список категорий:
```
category1 = Category.objects.create(category_name='книги на английском языке', 
category_description='современная проза на английском языке')

category2 = Category.objects.create(category_name='книги на русском языке', 
category_description='художественная литература на русском языке')

product1 = Product.objects.create(product_name='Casual Vacancy', 
product_description='Casual Vacancy Роулинг Д.К., роман о  маленьком городке.', 
category=category1, price=Decimal(1500))

product2 = Product.objects.create(product_name='The Queen`s Gambi', 
product_description='The Queen`s Gambit Tevis Walter, роман о жизни девушки-шахматного вундеркинда.', 
category=category1, price=Decimal(1750))

product3 = Product.objects.create(product_name='Я - посланник', 
product_description='Я - посланник Маркус Зусак, роман с захватывающей историей судьбы.', 
category=category2, price=Decimal(600))

product4 = Product.objects.create(product_name='Париж - всегда хорошая идея', 
product_description='Париж - всегда хорошая идея Барро Николя, история о люви.', 
category=category2, price=Decimal(570))
```

Сформируйте фикстуры для моделей Category и Product:
```
python -Xutf8 manage.py dumpdata catalog.Category catalog.Product --output catalog/fixtures/catalog_fixture.json --indent 4
```

Используйте кастомную команду для добавления 
тестовых продуктов с предварительной очисткой в [add_products.py](catalog/management/commands/add_products.py)

Добавьте информацию через админку на страницу с контактами.
