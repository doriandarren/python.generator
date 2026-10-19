from rest_framework.serializers import ModelSerializer
#from apps.devs.models import Devs


class DevSerializer(ModelSerializer):

    class Meta:
        # model = Dev
        ## fields = "__all__"
        fields = ['id', 'user_id','name','age','description']
