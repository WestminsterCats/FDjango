#
# Import
#

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, ItemType, Booking, IsCurrent, IsOverdue, ReservedStatus
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone

# Create your views here.

#
# Home
#


#
# Reservation, takes all items in the booking database and the equipment database and returns them to use when running the site.
#

@login_required
def reservations(request):
    item = Booking.objects.all()
    equipmentItem = Item.objects.all()

    context = {
        'item': item,
        'equipmentItem': equipmentItem
    }

    return render(request, 'equipment/reservations.html', context)

#
# Equipment
#

@login_required
def equipment(request):
    item = Item.objects.all()
    
    # Extract unique quantities and item types
    unique_quantities = set(item.quantity for item in item if item.quantity)
    unique_item_types = set(item.itemtype.type for item in item if item.itemtype)
    
    # Handle sorting
    sort_by = request.GET.get('sort_by')
    if sort_by == 'quantity':
        item = item.order_by('quantity')
    elif sort_by == 'itemtype':
        item = item.order_by('itemtype__type')
    
    context = {
        'item': item,
        'unique_quantities': sorted(unique_quantities),  # Sorts for ease on the eyes
        'unique_item_types': sorted(unique_item_types),  # Sorts for ease on the eyes
        'sort_by': sort_by  # Pass the current sort option to the template
    }
    
    return render(request, 'equipment/equipment.html', context)

#
# Item
#

@login_required
def item(request, id):
    listitem = Item.objects.get(id=id)
    context = {'listitem':listitem, 'item_id': id}

    return render(request, 'equipment/item.html', context)

#
# Reserve Item
#

from django.shortcuts import redirect

@login_required
def reserve_item(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        item_id = request.POST.get('item_id')  # Retrieve item ID from the form

        # Create a booking instance
        item = Item.objects.get(id=item_id)
        reservation_date = timezone.now().date()  # Get the current date
        return_date = reservation_date + timedelta(days=14)  # Calculate return date (two weeks later)
        
        booking = Booking.objects.create(
            user=request.user,
            item=item,
            isCurrent=IsCurrent.objects.get(isCurrent="Yes"),
            isOverdue=IsOverdue.objects.get(isOverdue="No"),
            reservedStatus=ReservedStatus.objects.get(status="Pending"),
            reservation_date=reservation_date,
            return_date=return_date
        )

        # Redirect to reservations page
        return redirect('/equipment/reservations')
    else:
        return JsonResponse({'message': 'Invalid request method'})

# equipment/views.py
from .models import import_items_from_excel

@login_required
def import_items_view(request):
    user = request.user
    if not user.is_superuser:
        return HttpResponse('403 Error: Access Denied')
    else:
        excel_file_path = 'equipment/static/equipment/EquipmentInventory.xlsx'
        import_items_from_excel(excel_file_path)
        return HttpResponse("Items imported successfully!")




