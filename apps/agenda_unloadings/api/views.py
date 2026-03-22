from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.agenda_unloadings.api.serializers import AgendaUnloadingSerializer
from apps.agenda_unloadings.models import AgendaUnloading


class AgendaUnloadingApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AgendaUnloadingSerializer
    queryset = AgendaUnloading.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
