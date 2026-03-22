from rest_framework.routers import DefaultRouter
from apps.agenda_unloadings.api.views import AgendaUnloadingApiViewSet

# Add urls.py:
# from apps.agenda_unloadings.api.router import router_agenda_unloading
# path('api/v1/', include(router_agenda_unloading.urls))


# example
router_agenda_unloading = DefaultRouter()

# examples
router_agenda_unloading.register(
    prefix='agenda_unloadings',
    basename='agenda_unloadings',
    viewset=AgendaUnloadingApiViewSet
)
