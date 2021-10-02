from django.urls import path

from . import views
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView, AllPostsFilterView, TagFilterView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("home", views.StartingPageView.as_view(), name="home"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/filter/<genre>", views.AllPostsFilterView.as_view(), name="posts-filter"),
    path("posts/by_tag/<tag_slug>", views.TagFilterView.as_view(), name="tag-filter", ),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"),  
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', 
    BlogDeleteView.as_view(), name='post_delete')

]