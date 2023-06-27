from rest_framework import serializers
from backend.huts.models import Huts, Approach, Month, Services, WeatherCondition


# class ShortApproachSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Approach
#         fields = "__all__"
#
#
# class ShortHutsSerializer(serializers.ModelSerializer):
#     approach = serializers.StringRelatedField(many=True, source="approach_set")
#     opened_in = serializers.StringRelatedField(many=True, source="opened_in_set")
#     services = serializers.StringRelatedField(many=True, source="services_set")
#     weather_condition = serializers.StringRelatedField(many=True, source="weather_condition_set")
#     class Meta:
#         model = Huts
#         fields = "__all__"


class ApproachSerializer(serializers.ModelSerializer):
    # huts = ShortHutsSerializer(many=True, read_only=True)

    class Meta:
        model = Approach
        fields = "__all__"


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = "__all__"


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = "__all__"


class HutsSerializer(serializers.ModelSerializer):
    approach = serializers.ManyRelatedField(child_relation=serializers.StringRelatedField())
    opened_in = serializers.ManyRelatedField(child_relation=serializers.StringRelatedField())
    services = serializers.ManyRelatedField(child_relation=serializers.StringRelatedField())
    weather_condition = serializers.ManyRelatedField(child_relation=serializers.StringRelatedField())

    class Meta:
        model = Huts
        fields = "__all__"
