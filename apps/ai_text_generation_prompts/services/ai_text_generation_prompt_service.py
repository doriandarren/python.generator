from apps.ai_text_generation_prompts.models import AiTextGenerationPrompt

class AiTextGenerationPromptService:

    def list(self):
        return AiTextGenerationPrompt.objects.all()


    def show(self, id):
        return AiTextGenerationPrompt.objects.filter(id=id).first()


    def findByIsProcessed(self, is_processed=False):
        return AiTextGenerationPrompt.objects.filter(is_processed=is_processed).first()


    def store(self, model: AiTextGenerationPrompt):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "system_role" in data:
            model.system_role = data["system_role"]
            
        
        if "system_message" in data:
            model.system_message = data["system_message"]
            
        
        if "user_role" in data:
            model.user_role = data["user_role"]
            
        
        if "user_message" in data:
            model.user_message = data["user_message"]
            
        
        if "is_processed" in data:
            model.is_processed = data["is_processed"]
            
        
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_ai_text_generation_prompt(
        self,
        system_role,
        system_message,
        user_role,
        user_message,
        is_processed,
    ) -> AiTextGenerationPrompt:
        model = AiTextGenerationPrompt()
        model.system_role = system_role
        model.system_message = system_message
        model.user_role = user_role
        model.user_message = user_message
        model.is_processed = is_processed

        return model
