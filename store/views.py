from django.shortcuts import render
from .models import Product

# Create your views here.


def store(request):
    """ A view to show all the products and
    sorting for the store page
    """
    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, 'store/store.html', context)


def products_by_category_view(request, category):
    """Filters for product categories"""
    products = Product.objects.filter(
        product_category_id__category_name=category)
    return render(request, "store/store.html", {"products": products})
