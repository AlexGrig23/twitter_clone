from django import forms
from posts.models import Post, Comment, User

class CommentForm(forms.Form):

    user = forms.ModelChoiceField(queryset=User.objects.all())
    post = forms.ModelChoiceField(queryset=Post.objects.all())
    content = forms.CharField(max_length=200, widget=forms.Textarea)


class PostForm(forms.Form):

    user = forms.ModelChoiceField(queryset=User.objects.all())
    title = forms.CharField(max_length=128)
    profile_picture = forms.ImageField()
    content = forms.CharField(max_length=200, widget=forms.Textarea)