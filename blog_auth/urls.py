from . import views
from django.urls import path

app_name = 'blog_auth'

urlpatterns = [
    path('blog_login', views.blog_login, name='login'),
    path('blog_logout', views.blog_logout, name='logout'),
    path('register', views.register, name='register')
]