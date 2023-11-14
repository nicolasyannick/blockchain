from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib import messages
from web3 import Web3

# Create your views here.


# Homepage Rendering
def home(request):
    # Fetch all products in the database
    products = Product.objects.all()
    # Fetch all orders in the database / Arrange by descending order_date
    orders = Order.objects.all().order_by('-order_date')

    # Getting the last 10 transactions from the Ethereum Network
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/0f27e0b2439f4a9887f2dc785011e634'))

    # Get the Last Block Number on the Ethereum Network
    if w3.is_connected():
        latest = w3.eth.block_number

        # Create an empty list to store the transactions
        transactions = []

        # For loop to display the last 20 blocks
        for i in range(latest, latest -3, -1):
            block = w3.eth.get_block(i, full_transactions=True)
        

        transactions.extend(block.transactions)

        transactions = transactions[:20]


    context={
        'products' : products,
        'orders' : orders,
        'transactions' : transactions,
    }

    return render(request, 'home.html', context)


# Placing the order
def place_order(request):
    if request.method == 'POST':
        # Retrieve order data from POST request
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        order_date = request.POST.get('order_date')

        order = Order(
            product_id = product_id,
            quantity = quantity,
            order_date = order_date,
        )

        order.save()

        return redirect('home')



    