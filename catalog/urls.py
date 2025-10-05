from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail, add_product
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>", product_detail, name="product_detail"),
    path("add_product/", add_product, name="add_product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
