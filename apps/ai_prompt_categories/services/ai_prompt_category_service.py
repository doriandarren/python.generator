from apps.ai_prompt_categories.models import AiPromptCategory

class AiPromptCategoryService:

    def list(self):
        return AiPromptCategory.objects.all()


    def show(self, id):
        return AiPromptCategory.objects.filter(id=id).first()


    def store(self, model: AiPromptCategory):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "name" in data:
            model.name = data["name"]
            
        
        if "description" in data:
            model.description = data["description"]
            
        
        if "slug" in data:
            model.slug = data["slug"]
            
        
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_ai_prompt_category(
        self,
        name,
        description,
        slug,
    ) -> AiPromptCategory:
        model = AiPromptCategory()
        model.name = name
        model.description = description
        model.slug = slug

        return model
