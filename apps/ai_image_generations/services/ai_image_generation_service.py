from apps.ai_image_generations.models import AiImageGeneration

class AiImageGenerationService:

    def list(self):
        return AiImageGeneration.objects.all()


    def show(self, id):
        return AiImageGeneration.objects.filter(id=id).first()


    def store(self, model: AiImageGeneration):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "ai_prompt_generation_id" in data:
            model.ai_prompt_generation_id = data["ai_prompt_generation_id"]
            
        
        if "comfyui_prompt_id" in data:
            model.comfyui_prompt_id = data["comfyui_prompt_id"]
            
        
        if "comfyui_output_path" in data:
            model.comfyui_output_path = data["comfyui_output_path"]
            
        
        if "mime_type" in data:
            model.mime_type = data["mime_type"]
            
        
        if "width" in data:
            model.width = data["width"]
            
        
        if "height" in data:
            model.height = data["height"]
            
        
        if "image_url" in data:
            model.image_url = data["image_url"]
            
        
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_ai_image_generation(
        self,
        ai_prompt_generation_id,
        comfyui_prompt_id,
        comfyui_output_path,
        mime_type,
        width,
        height,
        image_url,
    ) -> AiImageGeneration:
        model = AiImageGeneration()
        model.ai_prompt_generation_id = ai_prompt_generation_id
        model.comfyui_prompt_id = comfyui_prompt_id
        model.comfyui_output_path = comfyui_output_path
        model.mime_type = mime_type
        model.width = width
        model.height = height
        model.image_url = image_url

        return model
