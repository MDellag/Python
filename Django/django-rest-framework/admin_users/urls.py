from django.urls import include, path
from rest_framework import routers
from admin_users.users.views import UserViewSet
from admin_users.addresses.views import AddressViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'addresses', AddressViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
