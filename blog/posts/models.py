from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
import re
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
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    dislikes = models.ManyToManyField(User, blank=True, related_name="dislikes")

    def likes_count(self):
        return self.likes.count()
    
    def dislikes_count(self):
        return self.dislikes.count()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_details", kwargs={"pk": self.pk})
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    subscribers = models.ManyToManyField(
        User, related_name="subscribed_categories", blank=True
    )

    def is_subscribed(self, user): # check is user subscribe or Not
        return self.subscribers.filter(id=user.id).exists()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_details", kwargs={"category_id": self.pk})
    

class ForbiddenWords(models.Model):
    word = models.CharField(max_length=100)
    
    def save(self, *args,**kwargs):
        self.word = self.word.capitalize()
        return super().save(*args,**kwargs)
    def __str__(self):
        return self.word

class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    post_date  = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    
    def filter(self):
        forbidden_words = ForbiddenWords.objects.values_list("word",flat=True)
        pattern = re.compile(r"\b"+ '|'.join(re.escape(word) for word in forbidden_words) + r"\b" , flags=re.IGNORECASE)    
        self.content = re.sub(pattern, lambda x: '*' * len(x.group()), self.content)
        return self.content
    
    def save(self,*args, **kwargs):
        self.filter()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.content[:20]