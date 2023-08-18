from django.urls import path
from . import views
from .views import posts_list, comments_list, view_post, add_comment, comment_detail, add_post

urlpatterns = [

    path('', posts_list,  name="posts_list"),
    path('comments/<int:post_id>', comments_list, name="comments_list"),
    path('post/<int:post_id>/<int:user_id>/', view_post, name="view_post"),
    path('post/<int:user_id>/<int:post_id>/<int:comment_id>/', comment_detail, name="comment_detail"),
    path('post/add-comment/', add_comment, name="add_comment"),
    path('post/add-post/', add_post, name="add_post"),




]
