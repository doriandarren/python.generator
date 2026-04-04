from apps.ai_prompt_generations.models import AiPromptGeneration

class AiPromptGenerationService:

    def list(self):
        return AiPromptGeneration.objects.all()


    def show(self, id):
        return AiPromptGeneration.objects.filter(id=id).first()


    def findByIsProcessed(self):
        return AiPromptGeneration.objects.filter(is_text_processed=False).first()


    def store(self, model: AiPromptGeneration):
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
            
        
        if "is_text_processed" in data:
            model.is_text_processed = data["is_text_processed"]
            
        
        if "is_image_processed" in data:
            model.is_image_processed = data["is_image_processed"]
            
        
        if "is_video_processed" in data:
            model.is_video_processed = data["is_video_processed"]
            
        
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_ai_prompt_generation(
        self,
        system_role,
        system_message,
        user_role,
        user_message,
        is_text_processed=False,
        is_image_processed=False,
        is_video_processed=False,
    ) -> AiPromptGeneration:
        model = AiPromptGeneration()
        model.system_role = system_role
        model.system_message = system_message
        model.user_role = user_role
        model.user_message = user_message
        model.is_text_processed = is_text_processed
        model.is_image_processed = is_image_processed
        model.is_video_processed = is_video_processed

        return model
