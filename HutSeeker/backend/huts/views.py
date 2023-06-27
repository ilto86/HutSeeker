from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HutsSerializer, ApproachSerializer, MonthSerializer, ServicesSerializer, WeatherConditionSerializer
from .models import Huts, Approach, Month, Services, WeatherCondition

class HutsView(viewsets.ModelViewSet):
    serializer_class = HutsSerializer
    queryset = Huts.objects.all()


class ApproachView(viewsets.ModelViewSet):
    serializer_class = ApproachSerializer
    queryset = Approach.objects.all()


class MonthView(viewsets.ModelViewSet):
    serializer_class = MonthSerializer
    queryset = Month.objects.all()


class ServicesView(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()


class WeatherConditionView(viewsets.ModelViewSet):
    serializer_class = WeatherConditionSerializer
    queryset = WeatherCondition.objects.all()