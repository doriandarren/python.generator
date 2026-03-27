from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.ai_image_generations.api.serializers import AiImageGenerationSerializer
from apps.ai_image_generations.models import AiImageGeneration


class AiImageGenerationApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiImageGenerationSerializer
    queryset = AiImageGeneration.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
