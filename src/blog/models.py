from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User




class Post(models.Model):
    OPTIONS = {
        ('d', 'Draft'),
        ('p', 'Published')
    }
    
    CATEGORIES = {
        ('WORLD', 'world'),
        ('ENVIRONMENT', 'environment'),
        ('DESIGN','design' ),
        ('CULTURE','culture' ),
        ('BUSINESS','business' ),
        ('POLITICS','politics' ),
        ('OPINION','opinion' ),
        ('SCIENCE','science' ),
        ('HEALTH','health' ),
        ('TRAVEL','travel' ),
        ('STYLE','style' )
        
    }
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices = CATEGORIES, default = 'WORLD')
    image = models.CharField(max_length=1000, default= "https://www.start-business-online.com/images/thumbs/420_270/article_manager_uploads/blog.jpg")
    excerpt = models.CharField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    status = models.CharField(max_length=10, choices = OPTIONS, default = 'd')
    content = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
    
    def comment_count(self):
        return self.comment_set.all().count()
    def view_count(self):
        return self.postview_set.all().count()
    def like_count(self):
        return self.like_set.all().count()
    def comments(self):
        return self.comment_set.all()
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
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
