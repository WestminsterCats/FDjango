from django.contrib import admin
from .models import Item
from .models import ItemType
from .models import ItemLocation
from .models import ItemStatus
from .models import Booking
from .models import IsCurrent
from .models import ReservedStatus
from .models import IsOverdue

# # Register your models here.

admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(ItemLocation)
admin.site.register(ItemStatus)
admin.site.register(Booking)
admin.site.register(IsCurrent)
admin.site.register(ReservedStatus)
admin.site.register(IsOverdue)