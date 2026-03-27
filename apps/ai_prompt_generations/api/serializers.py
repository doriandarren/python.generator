from rest_framework.serializers import ModelSerializer
from apps.ai_prompt_generations.models import AiPromptGeneration


class aiPromptGenerationSerializer(ModelSerializer):

    class Meta:
        model = AiPromptGeneration
        ## fields = "__all__"
        fields = [
            'id', 
            'system_role',
            'system_message',
            'user_role',
            'user_message',
            'is_text_processed',
            'is_image_processed',
            'is_video_processed',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
