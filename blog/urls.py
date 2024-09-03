from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('community/<str:name>/', views.community_detail, name='community_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]