from django.http import HttpResponse
from users.models import User
from posts.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from users.forms import UserForm
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

def index(request):
    users = User.objects.all()
    context = {'users': users, 'title': 'List of users'}
    return render(request, 'users/users_list.html', context)


def user_detail(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, "users/user_detail.html", context)


def add_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user_data = form.cleaned_data

            if 'profile_pictures' in request.FILES:
                user_data['profile_pictures'] = request.FILES['profile_pictures']
            else:

                with open('static/img/default_user_image.png', 'rb') as f:
                    content = ContentFile(f.read())
                    user_data['profile_pictures'] = ImageFile(content, 'default_user_image.png')

            user = form.save()
            return redirect('user_detail', user_id=user.pk)

    else:
        form = UserForm()

    return render(request, 'users/create_user.html', {'form': form})



def users_list(request, username=None):
    if username:
        users = User.objects.filter(user__username=username)
        username = f"Lists of users by {username}"

    else:
        users = User.objects.all()
        username = "List of posts"

    context = {'users': users, 'username': username}
    return render(request, 'users/users_list.html', context)

def users_posts(request,user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(user=user)

    context = {
        'posts': posts,
        'user': user,
        'title': 'List of posts'
    }
    return render(request, 'users/users_posts.html', context)

