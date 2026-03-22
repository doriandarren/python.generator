from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserApiViewSet

# Add urls.py:
# from apps.users.api.router import router_user
# path('api/v1/', include(router_user.urls))


# example
router_user = DefaultRouter()

# examples
router_user.register(
    prefix='users',
    basename='users',
    viewset=UserApiViewSet
)
