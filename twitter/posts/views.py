from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import Post, Comment, User
from posts.forms import CommentForm, PostForm
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

def posts_list(request, username=None):

    if username:
        posts = Post.objects.filter(user__username=username)
        title = f"Lists of posts by {username}"

    else:
        posts = Post.objects.all()
        title = "List of posts"

    context = {'posts': posts, 'title': title }
    return render(request, 'posts/posts_list.html', context)


def comments_list(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)

    context = \
        {'comments': comments,
         'post': post,
         'title': 'List of comments'}
    return render(request, 'posts/comments_list.html', context)

def view_post(request, post_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post, 'user': user}

    return render(request, 'posts/view_post.html', context)


def add_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            post_data = form.cleaned_data

            if 'profile_picture' in request.FILES:
                post_data['profile_picture'] = request.FILES['profile_pictures']
            else:

                with open('static/img/default_cover_image.png', 'rb') as f:
                    content = ContentFile(f.read())
                    post_data['profile_picture'] = ImageFile(content, 'default_cover_image.png')

            post = Post.objects.create(**form.cleaned_data)
            return redirect('view_post', post_id=post.pk, user_id=post.user.pk)

    else:
        form = PostForm()
        return render(request, 'posts/create_post.html', {'form': form})




def comment_detail(request, user_id, post_id, comment_id):
    user = get_object_or_404(User, pk=user_id)
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    context = {'user': user, 'post': post, 'comment': comment}
    return render(request, "posts/comment_detail.html", context)



def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            comment = Comment.objects.create(**form.cleaned_data)
            return redirect('posts_list') # разобраться с редиректом когда хочу перейти на comment_detail выбивает ошибку не знаю где найти .

    else:
        form = CommentForm()
        return render(request, 'posts/create_comment.html', {'form': form})
