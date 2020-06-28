from django.db import models
from userinfo.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses= [("P","Published"),("D","Draft")]
    title = models.CharField(max_length=30)
    content = models.TextField()
    status = models.CharField(max_length=1,choices = statuses)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'blog/',blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title