from rest_framework.routers import DefaultRouter
from apps.ai_text_generation_prompts.api.views import AiTextGenerationPromptApiViewSet

# Add urls.py:
# from apps.ai_text_generation_prompts.api.router import router_ai_text_generation_prompt
# path('api/v1/', include(router_ai_text_generation_prompt.urls))


# example
router_ai_text_generation_prompt = DefaultRouter()

# examples
router_ai_text_generation_prompt.register(
    prefix='ai_text_generation_prompts',
    basename='ai_text_generation_prompts',
    viewset=AiTextGenerationPromptApiViewSet
)
