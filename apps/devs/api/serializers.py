from rest_framework.serializers import ModelSerializer
from apps.devs.models import Dev


class devSerializer(ModelSerializer):

    class Meta:
        model = Dev
        ## fields = "__all__"
        fields = ['id', 'a']
