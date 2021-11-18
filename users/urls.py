from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('profile/change', views.change_user_role, name='change_role'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/edit', views.edit_user, name='edit_profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
