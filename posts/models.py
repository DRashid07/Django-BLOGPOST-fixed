from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings



User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    view_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag',blank=True,related_name='posts')
    likes = models.ManyToManyField(User, blank=True,related_name='post_likes')
    favourites = models.ManyToManyField(User,blank=True,related_name='post_favourites')
    updated_at = models.DateTimeField(auto_now=True)
    reports=models.ManyToManyField(User, blank=True,related_name='post_reports')
    
    

    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user','post')
    
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user','post')

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def _str_(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    def _str_(self):
        return self.text[:20]
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.name

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user','post')

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title