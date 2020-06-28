from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique = True)
    bio = models.TextField(blank = True)
    image =  models.ImageField(upload_to ='profiles/',blank = True)
    is_author = models.BooleanField(blank = True)


    REQUIRED_FIELDS = ['email']


    def get_absolute_url(self):
        return reverse('profile',kwargs = {'id':self.id})

