from rest_framework import serializers
from .models import Order
from logistics.models import Shipment
  

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['tracking_number', 'status', 'shipped_at', 'delivered_at']



class OrderSerializer(serializers.ModelSerializer):
    shipment = ShipmentSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'