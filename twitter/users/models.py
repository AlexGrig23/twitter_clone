from django.db import models
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    profile_pictures = models.ImageField(upload_to="users/profile_images", null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("user_detail", kwargs={'pk': self.pk})