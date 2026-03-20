from rest_framework.routers import DefaultRouter
from apps.ai_text_generations.api.views import AiTextGenerationApiViewSet

# Add urls.py:
# from apps.ai_text_generations.api.router import router_ai_text_generation
# path('api/v1/', include(router_ai_text_generation.urls))


# example
router_ai_text_generation = DefaultRouter()

# examples
router_ai_text_generation.register(
    prefix='ai_text_generations',
    basename='ai_text_generations',
    viewset=AiTextGenerationApiViewSet
)
