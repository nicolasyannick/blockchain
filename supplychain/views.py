from django.shortcuts import render
from .models import Product, Order

# Create your views here.

def home(request):
    # Fetch all products in the database
    products = Product.objects.all()
    # Fetch all orders in the database
    orders = Order.objects.all()

    context={
        'products' : products,
        'orders' : orders,
    }

    return render(request, 'home.html', context)

    