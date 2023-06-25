from rest_framework import serializers
from .models import Huts, Approach

class HutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huts
        fields = "__all__"

class ApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approach
        fields = "__all__"
    