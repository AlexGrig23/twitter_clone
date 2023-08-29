from django import forms
from users.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email", "profile_pictures"]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "profile_pictures": forms.FileInput(attrs={'class': 'form-control'})
        }

