from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HutsSerializer, ApproachSerializer
from .models import Huts, Approach

class HutsView(viewsets.ModelViewSet):
    serializer_class = HutsSerializer
    queryset = Huts.objects.all()

class ApproachView(viewsets.ModelViewSet):
    serializer_class = ApproachSerializer
    queryset = Approach.objects.all()
