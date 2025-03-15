from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields you need
    profile_picture = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)
    blocked_users = models.ManyToManyField("self", symmetrical=False, related_name="blocked_by")

    def is_blocked_by(self, user):
        return self in user.blocked_users.all()
    def __str__(self):
        return self.username

class Chat(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    participants = models.ManyToManyField(CustomUser, related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)

