from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Tells Django that this serializer is based on the CustomUser model
        model = CustomUser
        # Specifies which fields to include in the serialized output
        fields = ["id", "username", "email", "profile_picture", "bio"]
