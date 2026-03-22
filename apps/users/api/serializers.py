from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class userSerializer(ModelSerializer):

    class Meta:
        model = User
        ## fields = "__all__"
        fields = [
            'id', 
            'email',
            'password',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
