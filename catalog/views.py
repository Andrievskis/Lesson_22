from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, ContactInfo


def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Продукт: {product.product_name}, описание: {product.product_description}, "
              f"категория: {product.category}, цена: {product.price}")


    return render(request, "home.html")


def contacts(request):
    try:
        contact_info = ContactInfo.objects.latest('created_at')
    except ContactInfo.DoesNotExist:
        contact_info = None

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение: {message} получено.")
    return render(request, "contacts.html", {"contact_info": contact_info})
