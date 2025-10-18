from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, CreateView

from catalog.models import Product, ContactInfo, Category


# def home(request):
#     latest_products = Product.objects.all().order_by('-created_at')
#     # latest_products = Product.objects.all()
#     paginator = Paginator(latest_products, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'product_list': page_obj,
#     }
#     # for product in latest_products:
#     #     print(f"Продукт: {product.product_name}, описание: {product.product_description}, "
#     #           f"категория: {product.category}, цена: {product.price}")
#     return render(request, "product_info.html", context)

class ProductListView(ListView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')


# def contacts(request):
#     try:
#         contact_info = ContactInfo.objects.latest('created_at')
#     except ContactInfo.DoesNotExist:
#         contact_info = None
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение: {message} получено.")
#     return render(request, "contacts.html", {"contact_info": contact_info})

class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request):
        try:
            contact_info = ContactInfo.objects.latest('created_at')
        except ContactInfo.DoesNotExist:
            contact_info = None

        return render(request, self.template_name, {'contact_info': contact_info})

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение: {message} получено.")


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product':product}
#     return render(request, "product_detail.html", context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# def add_product(request):
#     categories = Category.objects.all()
#     form_data = request.POST
#     files = request.FILES
#
#     if request.method == 'POST':
#         try:
#             product_data = {
#                 'product_name': form_data.get('product_name'),
#                 'product_description': form_data.get('product_description'),
#                 'category': Category.objects.get(id=form_data.get('category')),
#                 'price': form_data.get('price'),
#                 'image': files.get('image')
#             }
#
#             Product.objects.create(**product_data)
#             return redirect('catalog:home')
#
#         except Category.DoesNotExist:
#             return render(request, 'add_product.html', {'categories': categories})
#
#     return render(request, 'add_product.html', {'categories': categories})

class ProductCreateView(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = ['product_name', 'product_description', 'category', 'price']
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
