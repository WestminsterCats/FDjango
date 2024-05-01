#
# Import
#
from django.db import models
from django.contrib.auth.models import User
import openpyxl

# Create your models here.

#
# These are the models for the equipment system
#

class Item(models.Model):
    name = models.CharField(max_length=30)
    itemtype =models.ForeignKey('ItemType',on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(null=True)
    audit = models.DateField(null=True)
    itemlocation =models.ForeignKey('ItemLocation',on_delete=models.SET_NULL,null=True)
    itemstatus = models.ForeignKey("ItemStatus", on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class ItemType(models.Model):
    type = models.CharField(max_length=2000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type

class ItemLocation(models.Model):
    location = models.CharField(max_length=100000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location
    
class ItemStatus(models.Model):
    status = models.CharField(max_length=20000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status

#
# These are the models for the reservation system
#

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    isCurrent = models.ForeignKey('IsCurrent', on_delete=models.SET_NULL,null=True)
    isOverdue = models.ForeignKey('IsOverdue', on_delete=models.SET_NULL,null=True)
    reservedStatus = models.ForeignKey('ReservedStatus', on_delete=models.SET_NULL,null=True)
    reservation_date = models.DateField(auto_now=True)
    return_date = models.DateField(null=True)

#
# Is the reservation a current one or not?
#

class IsCurrent(models.Model):
    isCurrent = models.CharField(max_length=20000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.isCurrent

#
# Declined, Accepted or Pending?
#

class ReservedStatus(models.Model):
    status = models.CharField(max_length=2000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status

#
# Is it overdue or not?
#

class IsOverdue(models.Model):
    isOverdue = models.CharField(max_length=2000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.isOverdue

#
# This is the function I used to import the items from the excel file,
# it is commented out because it imports every time the server is run.
#

# def import_items_from_excel(file_path):
#     # Load the Excel file
#     wb = openpyxl.load_workbook(file_path)
#     sheet = wb.active

#     # Iterate over rows in the sheet (assuming the first row contains column headers)
#     for row in sheet.iter_rows(min_row=2, max_row=80, values_only=True):
#         name, type, quantity, audit, location, status, comments = row

#         # Create ItemType instance if not exists
#         item_type, _ = ItemType.objects.get_or_create(type=type)

#         # Create ItemLocation instance if not exists
#         item_location, _ = ItemLocation.objects.get_or_create(location=location)

#         # Create ItemStatus instance if not exists
#         if status:
#             item_status, _ = ItemStatus.objects.get_or_create(status=status)
#         else:
#             item_status = None

#         # Create Item instance
#         Item.objects.create(
#             name=name,
#             itemtype=item_type,
#             quantity=quantity,
#             audit=audit,
#             itemlocation=item_location,
#             itemstatus=item_status,
#             comments=comments
#         )

