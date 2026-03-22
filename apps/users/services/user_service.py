from apps.users.models import User

class UserService:

    def list(self):
        return User.objects.all()


    def show(self, id):
        return User.objects.filter(id=id).first()


    def store(self, model: User):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "email" in data:
            model.email = data["email"]
            
        
        if "password" in data:
            model.password = data["password"]
            
        
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_user(
        self,
        email,
        password,
    ) -> User:
        model = User()
        model.email = email
        model.password = password

        return model
