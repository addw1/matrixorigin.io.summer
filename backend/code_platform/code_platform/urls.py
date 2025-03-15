from django.urls import include, path

urlpatterns = [
    path("api/users", include("users.urls")),  # API endpoint prefix
    path("api/chat/", include("chat.urls")),  # Chat API endpoints
]