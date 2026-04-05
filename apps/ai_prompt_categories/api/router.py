from rest_framework.routers import DefaultRouter
from apps.ai_prompt_categories.api.views import AiPromptCategoryApiViewSet

# Add urls.py:
# from apps.ai_prompt_categories.api.router import router_ai_prompt_category
# path('api/v1/', include(router_ai_prompt_category.urls))


# example
router_ai_prompt_category = DefaultRouter()

# examples
router_ai_prompt_category.register(
    prefix='ai_prompt_categories',
    basename='ai_prompt_categories',
    viewset=AiPromptCategoryApiViewSet
)
