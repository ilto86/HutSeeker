from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HutsSerializer
from .models import Huts

class HutsView(viewsets.ModelViewSet):
    serializer_class = HutsSerializer
    queryset = Huts.objects.all()
