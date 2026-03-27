from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.ai_prompt_generations.api.serializers import AiPromptGenerationSerializer
from apps.ai_prompt_generations.models import AiPromptGeneration


class AiPromptGenerationApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiPromptGenerationSerializer
    queryset = AiPromptGeneration.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
