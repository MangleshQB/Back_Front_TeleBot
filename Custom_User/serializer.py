from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],


        )
        user.set_password(validated_data['password'])
        user.save()
        return user
