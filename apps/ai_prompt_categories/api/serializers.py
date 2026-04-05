from rest_framework.serializers import ModelSerializer
from apps.ai_prompt_categories.models import AiPromptCategory


class AiPromptCategorySerializer(ModelSerializer):

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
        ]
