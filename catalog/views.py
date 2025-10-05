from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product, ContactInfo, Category


def home(request):
    latest_products = Product.objects.all().order_by('-created_at')
    # latest_products = Product.objects.all()
    paginator = Paginator(latest_products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'product_list': page_obj,
    }
    # for product in latest_products:
    #     print(f"Продукт: {product.product_name}, описание: {product.product_description}, "
    #           f"категория: {product.category}, цена: {product.price}")
    return render(request, "product_info.html", context)


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


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product':product}
    return render(request, "product_detail.html", context)


def add_product(request):
    categories = Category.objects.all()
    form_data = request.POST
    files = request.FILES

    if request.method == 'POST':
        try:
            product_data = {
                'product_name': form_data.get('product_name'),
                'product_description': form_data.get('product_description'),
                'category': Category.objects.get(id=form_data.get('category')),
                'price': form_data.get('price'),
                'image': files.get('image')
            }

            Product.objects.create(**product_data)
            return redirect('catalog:home')

        except Category.DoesNotExist:
            return render(request, 'add_product.html', {'categories': categories})

    return render(request, 'add_product.html', {'categories': categories})
