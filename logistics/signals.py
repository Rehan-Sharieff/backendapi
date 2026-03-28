from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from .models import Shipment
import uuid
from datetime import date, timedelta


@receiver(post_save, sender=Order)
def create_shipment(sender, instance, created, **kwargs):
    if created:
        Shipment.objects.create(
            order=instance,
            tracking_number=str(uuid.uuid4())[:8].upper(),
            courier_name="Default Courier",
            estimated_delivery=date.today() + timedelta(days=5)
        )