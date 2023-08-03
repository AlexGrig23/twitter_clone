from django.db import models
from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)