from rest_framework import viewsets
from .models import CustomerRelations
from .serializers import CustomerRelationsSerializer
from rest_framework.permissions import IsAuthenticated


class CustomerRelationsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = CustomerRelations.objects.all()
    serializer_class = CustomerRelationsSerializer
