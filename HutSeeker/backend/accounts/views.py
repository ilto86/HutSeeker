from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from .serializers import AppUserSerializer, AppUserRegisterSerializer

UserModel = get_user_model()


# Class-based view for registering new users using generics.
# This view allows users to create new user objects with the provided data.
# class AppUserRegisterView(generics.CreateAPIView):

# Class-based view for registering new users using viewsets.
# This view provides the standard CRUD operations for user objects.
class AppUserRegisterView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()              # The queryset represents the list of all user objects.
    serializer_class = AppUserRegisterSerializer    # The serializer to be used for serialization/deserialization of data.
    permission_classes = (AllowAny,)                # The permission classes to determine who can access this view.


# Class-based view for retrieving, updating, and deleting user details using generics.
# This view allows users to retrieve, update, and delete user objects by their primary key.
# class AppUserDetailView(generics.RetrieveUpdateDestroyAPIView):

# Class-based view for retrieving, updating, and deleting user details using viewsets.
# This view provides the standard CRUD operations for user objects by their primary key.
class AppUserDetailView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()          # The queryset represents the list of all user objects.
    serializer_class = AppUserSerializer        # The serializer to be used for serialization/deserialization of data.
