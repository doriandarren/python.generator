from rest_framework.serializers import ModelSerializer
from apps.ai_text_generations.models import AiTextGeneration


class aiTextGenerationSerializer(ModelSerializer):

    class Meta:
        model = AiTextGeneration
        ## fields = "__all__"
        fields = ['id', 'user_id','model_name','system_message','user_message','response_message','response_done','response_done_reason','response_total_duration','response_load_duration','response_prompt_eval_count','response_prompt_eval_duration','response_eval_count','response_eval_duration']
