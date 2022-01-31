from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.urls import reverse


GENDER_CHOICES = (
    ('Erkak', 'Erkak'),
    ('Ayol', 'Ayol')
)



class User(AbstractUser):
    
    username = models.CharField('First name',
                                max_length=20, unique=True)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to="users-image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    REQUIRED_FIELDS = ['phone','email', 'password']

    def __str__(self):
        return "{} {}".format(self.username, self.last_name)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=20)
    followers = models.IntegerField()
    following = models.IntegerField()
    about = models.TextField(max_length=200)

    def __str__(self):
        return "Profile data of {} {}".format(self.user.username, self.user.last_name)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profilelar'


