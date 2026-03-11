from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


# Logic for the User
class RegisterUser(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

#Function for Post
class CreatePost(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

#Get all data
class PostList(generics.ListAPIView):
    queryset= Post.objects.all().order_by('-create_at')
    serializer_class=PostSerializer

#Updatation of Pst
class UpdatePost(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class=PostSerializer

#get post by ID
class PostDetail(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer

#In case of deleting the post
class DeletePost(generics.DestroyAPIView):
    queryset= Post.objects.all()
    serializer_class=PostSerializer
