from django import forms
from posts.models import Post, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["user", "post", "content"]
        widgets = {
            "user": forms.Select(attrs={'class': 'form-control'}),
            "post": forms.Select(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["user", "title", "profile_picture", "content"]
        widgets = {
            "user": forms.Select(attrs={'class': 'form-control'}),
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "profile_picture": forms.FileInput(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control'})
        }