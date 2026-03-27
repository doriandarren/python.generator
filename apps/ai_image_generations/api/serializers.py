from rest_framework.serializers import ModelSerializer
from apps.ai_image_generations.models import AiImageGeneration


class aiImageGenerationSerializer(ModelSerializer):

    class Meta:
        model = AiImageGeneration
        ## fields = "__all__"
        fields = [
            'id', 
            'ai_prompt_generation_id',
            'comfyui_prompt_id',
            'comfyui_output_path',
            'mime_type',
            'width',
            'height',
            'image_url',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
