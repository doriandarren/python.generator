from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.devs.api.serializers import DevSerializer
from apps.devs.models import Dev


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DevSerializer
    queryset = Dev.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
