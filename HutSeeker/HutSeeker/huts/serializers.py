from rest_framework import serializers
from .models import Huts

class HutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huts
        fields = (
            'id', 
            'hut_name', 
            'hut_owner', 
            'hut_care_taker', 
            'phone_contact',
            'hut_area',
            'altitude',
            'accommodation_beds',
            'approach',
            'weather_forecast',
            'opened_in',
            'services',
            'slug',
            'description',
            'website',
            'image',
            'longitude',
            'latitude',
            'publication_date_and_time',
            'user'
        )
