from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog_detail(request, blog_id):
    return render(request, 'blog_detail.html')


# 需要登入才能訪問頁面
@login_required()
# @login_required(login_url=reverse_lazy("blog_auth:login"))
def pub_blog(request):
    return render(request, 'pub_blog.html')
