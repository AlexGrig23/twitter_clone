from django.http import HttpResponse
from users.models import User
from posts.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from users.forms import UserForm
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.views.generic import ListView, DetailView, CreateView



class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = "users/user_detail.html"
    pk_url_kwarg = 'user_id'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create_user.html'


    def form_valid(self, form):
        user = form.save()

        if 'profile_pictures' in self.request.FILES:
            user.profile_pictures = self.request.FILES['profile_pictures']

        else:

            with open('static/img/default_user_image.png', 'rb') as f:
                content = ContentFile(f.read())
                user.profile_pictures.save('default_user_image.png', content)

        user.save()
        return redirect('user_detail', user_id=user.pk)



class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users_list.html'
    extra_context = {"title": 'USERS LIST'}

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username:
            return User.objects.filter(username=username)
        return User.objects.all()


class UserPostsDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/users_posts.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        user = User.objects.get(pk=user_id)
        posts = Post.objects.filter(user=user)

        context['posts'] = posts
        context['title'] = 'List of posts'
        return context