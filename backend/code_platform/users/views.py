from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

@api_view(["GET"])
def get_user_info(request, uid):
    try:
        user = User.objects.get(id=uid)  # Fetch user by ID
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)