from blog import views
from django.urls import path
from .views import PostListView

urlpatterns = [
    # path('',views.home, name='blog-home'),
    path('', PostListView.as_view(), name = 'blog-home'),
    path('about/',views.about, name='blog-about')
]