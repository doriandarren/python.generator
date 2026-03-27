from rest_framework.routers import DefaultRouter
from apps.ai_prompt_generations.api.views import AiPromptGenerationApiViewSet

# Add urls.py:
# from apps.ai_prompt_generations.api.router import router_ai_prompt_generation
# path('api/v1/', include(router_ai_prompt_generation.urls))


# example
router_ai_prompt_generation = DefaultRouter()

# examples
router_ai_prompt_generation.register(
    prefix='ai_prompt_generations',
    basename='ai_prompt_generations',
    viewset=AiPromptGenerationApiViewSet
)
