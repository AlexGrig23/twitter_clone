from django.urls import path
from . import views
from .views import PostListView, CommentListDetailView, PostDetailView, CommentCreateView, CommentDetailView, PostCreateView

urlpatterns = [

    path('', PostListView.as_view(),  name="posts_list"),
    path('comments/<int:post_id>', CommentListDetailView.as_view(), name="comments_list"),
    path('post/<int:post_id>/<int:user_id>/', PostDetailView.as_view(), name="view_post"),
    path('post/<int:user_id>/<int:post_id>/<int:comment_id>/', CommentDetailView.as_view(), name="comment_detail"),
    path('post/add-comment/', CommentCreateView.as_view(), name="add_comment"),
    path('post/add-post/', PostCreateView.as_view(), name="add_post"),



]
