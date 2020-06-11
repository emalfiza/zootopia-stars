from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products_by_category_view(request, category):
    """ Filters for product categories """
    products = Product.objects.filter(
        product_category_id__category_name=category)
    return render(request, "store/store.html", {"products": products})


def store(request):
    """ A view to show all the products and
    sorting for the store page
    """
    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)
