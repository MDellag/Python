from rest_framework import serializers
from admin_users.addresses.serializer import AddressSerializer

from admin_users.users.models import User


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['id', 'name', 'url']


class UserSerializer(serializers.ModelSerializer):
    # this is how we must nest serializers to indicate how we want to receive data
    # groups = GroupSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'dni', 'age', 'email', 'address']
