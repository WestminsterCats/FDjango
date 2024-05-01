from django.shortcuts import render

# Create your views here.

def cart(request):
    #Render the cart page
    return render(request, 'cart/cart.html')

def orders(request):
    #Render the order page
    return render(request, 'cart/orders.html')