from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator

from HutSeeker.accounts.manager import AppUserManager
from HutSeeker.utils.validators import validate_alphabet_characters


class AppUser(AbstractBaseUser, PermissionsMixin):
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 25
    LAST_NAME_MIN_LEN = 3

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='Email address',
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_alphabet_characters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_alphabet_characters,
        ),
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    last_login = models.DateTimeField(
        auto_now=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False
    )

    objects = AppUserManager()

    # User credentials consist of `email` and `password`
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_username()
