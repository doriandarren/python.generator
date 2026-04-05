from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.ai_prompt_categories.api.serializers import AiPromptCategorySerializer
from apps.ai_prompt_categories.models import AiPromptCategory


class AiPromptCategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiPromptCategorySerializer
    queryset = AiPromptCategory.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
