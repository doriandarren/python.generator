from rest_framework.serializers import ModelSerializer
from apps.ai_text_generation_prompts.models import AiTextGenerationPrompt


class aiTextGenerationPromptSerializer(ModelSerializer):

    class Meta:
        model = AiTextGenerationPrompt
        ## fields = "__all__"
        fields = ['id', 'system_role','system_message','user_role','user_message','is_processed']
