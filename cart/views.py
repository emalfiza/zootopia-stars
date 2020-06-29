from django.shortcuts import render
from order.models import Order

# Create your views here.


def cart(request):
    """ See contents of cart also queries if the user exist
    otherwise creates one """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'cart/cart.html', context)
