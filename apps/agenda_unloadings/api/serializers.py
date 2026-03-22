from rest_framework.serializers import ModelSerializer
from apps.agenda_unloadings.models import AgendaUnloading


class agendaUnloadingSerializer(ModelSerializer):

    class Meta:
        model = AgendaUnloading
        ## fields = "__all__"
        fields = [
            'id', 
            'user_id',
            'name',
            'age',
            'description',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
