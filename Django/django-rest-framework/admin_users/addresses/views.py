from rest_framework import viewsets, permissions

from admin_users.addresses.models import Address
from admin_users.addresses.serializer import AddressSerializer

# Create your views here.


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
