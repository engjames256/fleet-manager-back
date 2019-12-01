from rest_framework import serializers
from .models import CustomerRelations


class CustomerRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRelations
        fields = "__all__"
