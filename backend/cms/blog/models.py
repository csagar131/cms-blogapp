from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce import models as tinymce_models
from accounts.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(blank = True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Post(models.Model):
    statuses = [
        ('D','Draft'),
        ('P','Published'),
    ]
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique = True,blank = True)
    content = tinymce_models.HTMLField()
    date =  models.CharField(max_length=30)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=statuses)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    images = models.ImageField(upload_to="blog/post",blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'slug':self.slug})
