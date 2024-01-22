from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from .utils import get_all_user_permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import Http404

# Create your views here.

def get_auth_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'user':UserLoginSerializer(user).data,
        'permission':get_all_user_permissions(user),
        'refresh': str(refresh),
        'token': str(refresh.access_token) 
    }
    

class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if not user:
            response_data = {'message':'Invalid Credential'}
            return Response(response_data, status=400)
        
        user_data = get_auth_for_user(user)
        return Response(user_data, status=200)
    
    

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
       data = request.data
       serializer = UserRegistrationSerializer(data=data)
       if serializer.is_valid():
           user = serializer.save()
           user_data = get_auth_for_user(user)
           return Response(user_data, status=201)
       else:
           error_response = {
                "message": serializer.errors  
            }
           return Response(error_response, status=status.HTTP_400_BAD_REQUEST)


# create post and get all created posts
class PostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            error_response = {
                "message": serializer.errors  
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

# get post detail
class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
# get the post object model
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404("Post not found")

        
# retrieve a single post by id using primary key (pk)
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
# update a post by id using primary key (pk)
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            error_response = {
                "message": serializer.errors  
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    
# delete a post by id using primary key (pk)
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        success_response = {
            "message": "post deleted successfully" 
        }
        return Response(success_response,status=200)
    
    
        