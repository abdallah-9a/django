from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    pic = models.CharField(max_length=100)
    tages = TaggableManager()
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    subscribers = models.ManyToManyField(
        User, related_name="subscribed_categories", blank=True
    )

    def is_subscribed(self, user): # check is user subscribe or Not
        return self.subscribers.filter(id=user.id).exists()

    def __str__(self):
        return self.name
