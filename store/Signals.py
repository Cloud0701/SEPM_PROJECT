from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import *

def CreateCustomer(sender,instance,created, **kwargs):
	if created:
		Customer.objects.create(
            user=instance,
            name = instance.username,
        )
		
post_save.connect(CreateCustomer,sender=User)

def CreateOrder(sender,instance,created, **kwargs):
	if created:
		Order.objects.create(
            user=instance,
            name = instance.username,
        )
		
post_save.connect(CreateOrder,sender=User)


