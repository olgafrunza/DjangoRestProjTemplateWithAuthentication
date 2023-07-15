from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='default.png', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def view_count(self):
        return self.postviewrecords_set.count()
    @property
    def like_count(self):
        return self.like_set.count()
    @property
    def comment_count(self):
        return self.comment_set.count()
    @property
    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)   
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title} - {self.commentor.username}"
    

class PostViewRecords(models.Model):
    created = models.DateTimeField(auto_now_add=True)   
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title} - {self.viewer.username}"    
    

class Like(models.Model): 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title} - {self.liker.username}"        