from django.urls import path
from . import views #. means the current directory
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

#basically copied the project level urls.py
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  #name isnt just set to 'home' because it may clash with other app homepages
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), 
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about,name='blog-about'),
]




























