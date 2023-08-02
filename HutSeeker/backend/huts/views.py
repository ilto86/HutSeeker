from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .serializers import HutsSerializer, ApproachSerializer, MonthSerializer, ServicesSerializer, WeatherConditionSerializer
from .models import Huts, Approach, Month, Services, WeatherCondition


class HutsListCreateView(viewsets.ModelViewSet):
    serializer_class = HutsSerializer
    queryset = Huts.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class HutsDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Huts.objects.all()
    serializer_class = HutsSerializer

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(queryset, pk=pk, slug=slug)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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