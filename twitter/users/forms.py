from django import forms
from users.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=50, label="Enter user name")
    email = forms.EmailField(max_length=100, label="Enter user email")
    profile_pictures = forms.ImageField(label="Download user photo", required=False)
