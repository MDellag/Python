from rest_framework import serializers

from admin_users.addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'nro', 'city']
