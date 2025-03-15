from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import CustomUser, Chat

@api_view(["POST"])
def change_chat(request):
    """
    Handles chat switching and checks if the user is blocked.
    """
    data = request.data
    chat_id = data.get("chatId")
    user_id = data.get("userId")

    current_user = request.user
    chat_user = get_object_or_404(CustomUser, id=user_id)

    if chat_user.is_blocked_by(current_user):
        return Response({
            "chatId": chat_id,
            "user": None,
            "isCurrentUserBlocked": True,
            "isReceiverBlocked": False
        }, status=403)

    if current_user.is_blocked_by(chat_user):
        return Response({
            "chatId": chat_id,
            "user": {
                "id": chat_user.id,
                "username": chat_user.username
            },
            "isCurrentUserBlocked": False,
            "isReceiverBlocked": True
        }, status=403)

    return Response({
        "chatId": chat_id,
        "user": {
            "id": chat_user.id,
            "username": chat_user.username
        },
        "isCurrentUserBlocked": False,
        "isReceiverBlocked": False
    })

@api_view(["POST"])
def toggle_block(request):
    """
    Toggle block status between users.
    """
    data = request.data
    user_id = data.get("userId")
    current_user = request.user
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user in current_user.blocked_users.all():
        current_user.blocked_users.remove(target_user)
        is_receiver_blocked = False
    else:
        current_user.blocked_users.add(target_user)
        is_receiver_blocked = True

    return Response({"isReceiverBlocked": is_receiver_blocked})

@api_view(["POST"])
def reset_chat(request):
    """
    Resets the chat session.
    """
    return Response({
        "chatId": None,
        "user": None,
        "isCurrentUserBlocked": False,
        "isReceiverBlocked": False
    })

