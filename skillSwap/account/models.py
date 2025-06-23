from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, full_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            full_name = full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            full_name = full_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    full_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    date_of_birth   = models.DateField(null=True,blank=True)
    phone_number    = models.CharField(max_length=50)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    Gender = {
        'm':'Male',
        'f':'female',
        'o':'other'
    }
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    permanent_address = models.CharField(blank=True, max_length=100)
    temporary_address = models.CharField(blank=True, max_length=100)
    gender = models.CharField(choices=Gender, default='Select gender')
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    skill = models.CharField(blank=True, max_length=20)
    experience = models.TextField()
    personality = models.TextField()

    def __str__(self):
        return self.user.full_name

