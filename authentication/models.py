from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from simple_history.models import HistoricalRecords
from authentication.manager import UserManager
from base.models import BaseModel


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Email'
    )
    is_active = models.BooleanField(
        default=True
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Base User'
        verbose_name_plural = 'Base Users'


class Consultant(BaseModel):
    user = models.OneToOneField(
        'authentication.BaseUser',
        related_name='consultant',
        on_delete=models.PROTECT,
    )
    historic = HistoricalRecords(
        related_name='consultant_historic'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Name'
    )

    def __str__(self):
        return f"{self.user.email}"
