import datetime
from datetime import date

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('Correo Electronico Obligatorio')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    if extra_fields.get('is_staff') is not True:
      raise ValueError('El superusuario debe tener is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('El superusuario debe tener is_superuser=True.')
    superuser = SuperUser(email=email, **extra_fields)
    superuser.set_password(password)
    superuser.save(using=self._db)
    return superuser


class CustomUser(AbstractUser):
  birth_day = models.DateField(_('Fecha Nacimiento'))
  first_name = models.CharField(_('Nombre'), max_length=30)
  last_name = models.CharField(_('Apellido'), max_length=30)
  username = models.CharField(_('Usuario'), max_length=20, unique=True)
  email = models.EmailField(_('Correo Electrónico'), unique=True)
  is_staff = models.BooleanField(_('Admin'), default=False)
  is_active = models.BooleanField(_('Activo'), default=True)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['birth_day', 'first_name', 'last_name', 'username']

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'

  def __str__(self):
    return self.email


class SuperUser(CustomUser):
  class Meta:
    verbose_name = 'Super Usuario'
    verbose_name_plural = 'Super Usuarios'


class User(CustomUser):
  class Meta:
    verbose_name = 'Usuario Normal'
    verbose_name_plural = 'Usuarios Normales'


class Blog(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  image = models.ImageField(upload_to='blogs_Julissa/images')
  date = models.DateField(default=datetime.date.today)

  def __str__(self) -> str:
    return self.title


class Portfolio(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='portfolio_Julissa/images')
  url = models.URLField(blank=True)
  date = models.DateField(default=date.today)

  def __str__(self) -> str:
    return self.title


class Curso(models.Model):
  institucion_del_curso = models.CharField(max_length=225)
  descripcion_curso = models.TextField()
  fecha_curso = models.DateField()
  numero_horas = models.PositiveIntegerField()

  def __str__(self):
    return f'{self.descripcion_curso} - {self.institucion_del_curso}'
