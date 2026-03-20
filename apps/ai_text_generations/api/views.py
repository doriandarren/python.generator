from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.ai_text_generations.api.serializers import AiTextGenerationSerializer
from apps.ai_text_generations.models import AiTextGeneration


class AiTextGenerationApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiTextGenerationSerializer
    queryset = AiTextGeneration.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
