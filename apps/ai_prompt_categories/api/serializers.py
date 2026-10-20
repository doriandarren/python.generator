from rest_framework.serializers import ModelSerializer
from apps.ai_prompt_categories.models import AiPromptCategory
from apps.ai_prompt_generations.api.serializers import AiPromptGenerationSerializer


class AiPromptCategorySerializer(ModelSerializer):
    
    ai_prompt_generations = AiPromptGenerationSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = AiPromptCategory
        ## fields = "__all__"
        fields = [
            'id', 
            'name',
            'description',
            'slug',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            "ai_prompt_generations",  # Relación 1:N
        ]
