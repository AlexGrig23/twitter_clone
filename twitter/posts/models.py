from django.db import models
from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="posts/profile_images", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200, null=True, blank=True)
    cover_image = models.ImageField(upload_to="posts/covers", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
