from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('email', 'password', 'first_name', 'last_name', 'username')
