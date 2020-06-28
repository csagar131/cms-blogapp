from django.urls import path,include
# from blog.views import PostListCreateAPIVIew,PostRetrieveUpdateDestroyAPIView
from blog.views import PostModelViewSet
from rest_framework.routers import DefaultRouter


blog_router = DefaultRouter()
blog_router.register('posts',PostModelViewSet)

urlpatterns = [
    path('',include(blog_router.urls)),
]