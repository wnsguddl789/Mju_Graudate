from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager
from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, addmission, major, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            addmission=addmission,
            major = major,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, addmission, major, password):
        user = self.create_user(
            email,
            password=password,
            name = name,
            addmission=addmission,
            major = major,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    password   = models.CharField(max_length = 64,verbose_name = "비밀번호")
    name       = models.CharField(max_length = 20,null=True,default='')
    addmission = models.CharField(max_length = 20,null=True,default='')
    major      = models.CharField(max_length = 20,null=True,default='')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['addmission']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
