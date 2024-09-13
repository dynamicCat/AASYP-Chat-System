from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    timezone = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    oauth_provider = models.CharField(max_length=50, blank=True, null=True)
    oauth_provider_id = models.CharField(max_length=255, blank=True, null=True)
    oauth_access_token = models.CharField(max_length=500, blank=True, null=True)

    # 添加 related_name 以避免与 auth.User 中的冲突
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # 确保 related_name 唯一
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # 确保 related_name 唯一
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
