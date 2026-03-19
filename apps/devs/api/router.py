from rest_framework.routers import DefaultRouter
from apps.devs.api.views import DevApiViewSet

# Add urls.py:
# from apps.devs.api.router import router_dev
# path('api/v1/', include(router_dev.urls))


# example
router_dev = DefaultRouter()

# examples
router_dev.register(
    prefix='devs',
    basename='devs',
    viewset=DevApiViewSet
)
