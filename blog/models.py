from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))



class Community(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
    
class JoinCommunity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joining_community")
    join_community = models.ManyToManyField(Community)
    join = models.BooleanField()

    def __str__(self):
        return f"{self.user.username}"

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community", default=None, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body}"