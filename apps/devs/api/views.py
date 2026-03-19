from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from core.cron.cron import hello_cron
#from django_filters.rest_framework import DjangoFilterBackend

#from apps.devs.api.serializers import DevSerializer
#from apps.devs.models import Dev


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # serializer_class = DevSerializer
    # queryset = Dev.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
    
    
    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):
        
        hello_cron()
        
        return Response({
            'message': "OK",
        })
    
