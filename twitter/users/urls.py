from django.urls import path

from .views import index, add_user, user_detail, users_list, users_posts

urlpatterns = [
    path('', index,  name="index"),
    path('users/<int:user_id>', user_detail, name="user_detail"),
    path('users/add-user', add_user, name="add_user"),
    path('users/users-list', users_list, name="users_list"),
    path('users/users-posts/<int:user_id>', users_posts, name='users_posts')


]
