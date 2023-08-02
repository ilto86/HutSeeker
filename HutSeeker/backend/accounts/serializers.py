from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser')


class AppUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
