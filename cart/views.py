from django.shortcuts import render

# Create your views here.

def cart(request):
    #Render the cart page
    return render(request, 'cart/cart.html')