from django.contrib import admin
from django.urls import path,include
from blog.views import IndexView,CategoryIndexView,BlogDetailView,ContactFormView,PostModelFormView,PostFormUpdateView,PostDeleteView

urlpatterns = [
    path('',IndexView.as_view()),
    path('contactus',ContactFormView.as_view(),name = 'contact-us'),
    path('posts',PostModelFormView.as_view(),name = 'new-post'),
    path('posts/<slug:slug>',PostFormUpdateView.as_view(),name = 'update-post'),
    path('<slug:slug>',BlogDetailView.as_view(), name = 'post-detail'),
    path('delete/<slug:slug>',PostDeleteView.as_view(),name='delete-post'),
]
