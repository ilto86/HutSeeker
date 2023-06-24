from rest_framework import fields, serializers
from .models import Huts
from .models import Approach, Month, Services

class HutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huts
        fields = "__all__"
    