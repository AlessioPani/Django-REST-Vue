# Version with WebAPI (JSON Format)
from .models import Manufacturer, Product
from django.http import JsonResponse


def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())}  # values("pk", "name")
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity
            }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Product not found."
            }},
            status=404)
    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    data = {"manufacturers": list(manufacturers.values())}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        products = manufacturer.products.all()
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "products": list(products.values('name',
                                             'description',
                                             'price',
                                             'shipping_cost',
                                             'quantity',
                                             'photo'))
            }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Manufacturer not found."
            }},
            status=404)
    return response

# Version without WebAPI #
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from .models import Manufacturer, Product


# class ProductDetailView(DetailView):
#     model = Product
#     context_object_name = 'product'
#     template_name = "product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     context_object_name = 'products'
#     template_name = "product_list.html"
