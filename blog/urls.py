from django.urls import path
from .views import *

urlpatterns= [
    path('register/',RegisterUser.as_view()),
    path('posts/create/',CreatePost.as_view()),
    path('post/all/',PostList.as_view()),
    path('post<int:pk>/',PostDetail.as_view()),
    path('post/update/<int:pk>/',UpdatePost.as_view()),
    path('post/delete/<int:pk>/',DeletePost.as_view()),
]