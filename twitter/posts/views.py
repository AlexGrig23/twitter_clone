from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import Post, Comment, User
from posts.forms import CommentForm, PostForm
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.views.generic import ListView, DetailView, CreateView



class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts_list.html'
    extra_context = {'title': 'POSTS LIST'}

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username:
            return Post.objects.filter(username=username)
        return Post.objects.all()


class CommentListDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/comments_list.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = Comment.objects.filter(post=post)

        context['comments'] = comments
        context['title'] = 'COMMENTS LIST'
        return context



class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/view_post.html'
    pk_url_kwarg = 'post_id'


    def get_object(self, queryset=None):
        post_id = self.kwargs.get('post_id')
        user_id = self.kwargs.get('user_id')  # user_id будет вторым параметром в URL
        return get_object_or_404(Post, pk=post_id, user__pk=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        context['user'] = user
        return context





class PostCreateView(CreateView):
    model = User
    form_class = PostForm
    template_name = 'posts/create_post.html'


    def form_valid(self, form):
        post = form.save()

        if 'profile_picture' in self.request.FILES:
            post.profile_picture = self.request.FILES['profile_picture']

        else:

            with open('static/img/default_user_image.png', 'rb') as f:
                content = ContentFile(f.read())
                post.profile_picture.save('default_user_image.png', content)

        post.save()
        return redirect('view_post', post_id=post.pk, user_id=post.user.pk)





class CommentDetailView(DetailView):
    model = Comment
    context_object_name = 'post'
    template_name = 'posts/comment_detail.html'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('user_id')
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(Comment, pk=comment_id, post__user__pk=user_id, post__pk=post_id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        user = get_object_or_404(User, pk=user_id)
        post = get_object_or_404(Post, pk=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        context['user'] = user
        context['post'] = post
        context['comment'] = comment
        return context



class CommentCreateView(CreateView):
    model = Comment
    form = CommentForm
    template_name = 'posts/create_comment.html'
    fields = ['user', 'post', 'content']

