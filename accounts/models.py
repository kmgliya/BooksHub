from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext as _


class JustUser(AbstractUser):
    ...

#     email = models.EmailField(_('email address'), unique=True)
#
#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[AbstractUser.username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#         null=True,
#         blank=True,
#     )
#
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )
#
#     def __str__(self):
#         return self.username
