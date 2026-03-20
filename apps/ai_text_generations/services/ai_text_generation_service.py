from apps.ai_text_generations.models import AiTextGeneration


class AiTextGenerationService:
    
    def list(self):
        return AiTextGeneration.objects.all()
    
    
    def show(self, id):
        return AiTextGeneration.objects.filter(id=id).first()
    
    
    def store(self, model: AiTextGeneration):
        model.save()
        return model
    
    
    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "user_id" in data:
            model.user_id = data["user_id"]

        if "model_name" in data:
            model.model_name = data["model_name"]

        if "system_message" in data:
            model.system_message = data["system_message"]

        if "user_message" in data:
            model.user_message = data["user_message"]

        if "response_message" in data:
            model.response_message = data["response_message"]

        if "response_done" in data:
            model.response_done = data["response_done"]

        if "response_done_reason" in data:
            model.response_done_reason = data["response_done_reason"]

        if "response_total_duration" in data:
            model.response_total_duration = data["response_total_duration"]

        if "response_load_duration" in data:
            model.response_load_duration = data["response_load_duration"]

        if "response_prompt_eval_count" in data:
            model.response_prompt_eval_count = data["response_prompt_eval_count"]

        if "response_prompt_eval_duration" in data:
            model.response_prompt_eval_duration = data["response_prompt_eval_duration"]

        if "response_eval_count" in data:
            model.response_eval_count = data["response_eval_count"]

        if "response_eval_duration" in data:
            model.response_eval_duration = data["response_eval_duration"]

        model.save()
        return model
    
    

    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True
    
    
    
    def set_ai_text_generation(
        self,
        user_id,
        model_name,
        system_message,
        user_message,
        response_message,
        response_done,
        response_done_reason,
        response_total_duration,
        response_load_duration,
        response_prompt_eval_count,
        response_prompt_eval_duration,
        response_eval_count,
        response_eval_duration,
    ) -> AiTextGeneration:
        model = AiTextGeneration()
        model.user_id = user_id
        model.model_name = model_name
        model.system_message = system_message
        model.user_message = user_message
        model.response_message = response_message
        model.response_done = response_done
        model.response_done_reason = response_done_reason
        model.response_total_duration = response_total_duration
        model.response_load_duration = response_load_duration
        model.response_prompt_eval_count = response_prompt_eval_count
        model.response_prompt_eval_duration = response_prompt_eval_duration
        model.response_eval_count = response_eval_count
        model.response_eval_duration = response_eval_duration
        
        return model
