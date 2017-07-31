import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Username', max_length=30, unique=True, validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                      "usuario pode contem somente letras, digitos ou @/./+/-/_", 'invalid')
        ]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Full Name', max_length=100, blank=True)

    is_active = models.BooleanField('Está Ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da Equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    profilePic = models.ImageField(
        upload_to='accounts/profiles', verbose_name='Profile picture',
        null=True, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
