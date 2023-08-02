from .models import *
from rest_framework import serializers


class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class productsserializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

        depth = 1
