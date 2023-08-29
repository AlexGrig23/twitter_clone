from django.urls import path

from .views import UserCreateView, UserDetailView, UserListView, UserPostsDetailView

urlpatterns = [
    # path('', index,  name="index"),
    path('users/<int:user_id>', UserDetailView.as_view(), name="user_detail"),
    path('users/add-user', UserCreateView.as_view(), name="add_user"),
    path('users/users-list', UserListView.as_view(), name="users_list"),
    path('users/users-posts/<int:user_id>', UserPostsDetailView.as_view(), name='users_posts')

]
