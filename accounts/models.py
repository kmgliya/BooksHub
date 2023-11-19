from django.contrib.auth.models import AbstractUser
from django.db import models


class Just_User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='JustUserUserPermissions',
        blank=True,
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='just_user_groups',
        blank=True,
    )

    def __str__(self):
        return self.username
