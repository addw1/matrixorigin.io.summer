from django.urls import path
from .views import change_chat, toggle_block, reset_chat

urlpatterns = [
    path("change_chat/", change_chat, name="change_chat"),
    path("toggle_block/", toggle_block, name="toggle_block"),
    path("reset_chat/", reset_chat, name="reset_chat"),
]