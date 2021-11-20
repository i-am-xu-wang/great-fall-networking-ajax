from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('profile/change', views.change_user_role, name='change_role'),
    path('<str:username>/profile', views.profile, name='profile'),
    path('<str:username>/profile/edit', views.edit_user, name='edit_profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('post-comment', views.post_comment, name='post_comment'),
    path('<int:comment_id>/edit', views.edit_comment, name='edit_comment'),
    path('delete', views.delete_comment, name='delete_comment'),
]
