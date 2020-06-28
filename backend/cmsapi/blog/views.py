from django.shortcuts import render
from blog.models import Post,Category
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostSerializer,CategorySerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from blog.permissions import IsAuthorOrReadOnly


class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authenication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,DjangoModelPermissions,IsAuthorOrReadOnly]






# class PostAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         posts = Post.objects.all()
#         ser_obj = PostSerializer(posts,many=True)
#         return Response(ser_obj.data)


#     def post(self,request,*args,**kwargs):
#         ser_obj = PostSerializer(data = request.data)
#         if ser_obj.is_valid():
#             post_obj =  ser_obj.save()
#             post_ser = PostSerializer(post_obj)
#             return Response(post_ser.data,status = status.HTTP_201_CREATED)
#         return Response(ser_obj.errors,status = status.HTTP_400_BAD_REQUEST)


# class PostListCreateAPIVIew(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



