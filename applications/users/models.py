from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculio'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    username = models.CharField(max_length=30,unique=True)
    email= models.EmailField(unique=True)
    fullname = models.CharField('Nombres',max_length=100)
    genero = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    datebirth = models.DateTimeField('Fecha Nacimiento',blank=True,null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return str(self.pk) + '-' + self.fullname

