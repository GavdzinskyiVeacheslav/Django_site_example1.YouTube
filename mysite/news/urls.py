from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Articles
from django.urls import path

urlpatterns = [
    path("", ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    path('<int:pk>', DetailView.as_view(model=Articles, template_name="news/post.html")),

]