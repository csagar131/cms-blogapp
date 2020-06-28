from rest_framework.authtoken import views
from django.urls import path,include

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]