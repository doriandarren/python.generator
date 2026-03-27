from rest_framework.routers import DefaultRouter
from apps.ai_image_generations.api.views import AiImageGenerationApiViewSet

# Add urls.py:
# from apps.ai_image_generations.api.router import router_ai_image_generation
# path('api/v1/', include(router_ai_image_generation.urls))


# example
router_ai_image_generation = DefaultRouter()

# examples
router_ai_image_generation.register(
    prefix='ai_image_generations',
    basename='ai_image_generations',
    viewset=AiImageGenerationApiViewSet
)
