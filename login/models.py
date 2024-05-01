from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add your additional fields here
    isApproved = models.IntegerField(blank=False, default=0)
    alerts = models.IntegerField(blank=True, default=0)
    # Add more fields as needed

    def __str__(self):
        return self.user.username