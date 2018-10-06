from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    url = models.TextField( max_length=450,null=True, verbose_name="")
    pub_date = models.DateTimeField(null=True, default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:postshome')
