from apps.agenda_unloadings.models import AgendaUnloading

class AgendaUnloadingService:

    def list(self):
        return AgendaUnloading.objects.all()


    def show(self, id):
        return AgendaUnloading.objects.filter(id=id).first()


    def store(self, model: AgendaUnloading):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "user_id" in data:
            model.user_id = data["user_id"]
            
        
        if "name" in data:
            model.name = data["name"]
            
        
        if "age" in data:
            model.age = data["age"]
            
        
        if "description" in data:
            model.description = data["description"]
            
        
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_agenda_unloading(
        self,
        user_id,
        name,
        age,
        description,
    ) -> AgendaUnloading:
        model = AgendaUnloading()
        model.user_id = user_id
        model.name = name
        model.age = age
        model.description = description

        return model
