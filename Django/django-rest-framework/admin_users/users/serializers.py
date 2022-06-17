from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'url']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # this is how we must nest serializers to indicate how we want to receive data
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
