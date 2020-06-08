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
