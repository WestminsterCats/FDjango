from django.shortcuts import render

# Create your views here.
def currentholdings(request):
    #Render the current holdings page
    return render(request, 'currentholdings/currentholdings.html')