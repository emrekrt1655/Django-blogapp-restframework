from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIRONMENT = 'environment'
    DESIGN = 'design'
    CULTURE = 'culture'
    BUSINESS = 'business'
    POLITICS = 'politics'
    OPINION = 'opinion'
    SCIENCE = 'science'
    HEALTH = 'health'
    STYLE = 'style'
    TRAVEL = 'travel'



class Post(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    category = models.CharField(max_length=50, choices = Categories.choices, default = Categories.WORLD)    
    image = models.CharField(max_length=1000, default= "https://www.start-business-online.com/images/thumbs/420_270/article_manager_uploads/blog.jpg")
    excerpt = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    published =models.BooleanField(default=False)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    
        
    def __str__ (self):
        return self.title
    @property
    def comment_count(self):
        return self.comment_set.all().count()
    @property
    def view_count(self):
        return self.postview_set.all().count()
    @property
    def like_count(self):
        return self.like_set.all().count()
    @property
    def comments(self):
        return self.comment_set.all()
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='Add Comment...')
    
    def __str__(self):
        return self.user.username
    
     
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
