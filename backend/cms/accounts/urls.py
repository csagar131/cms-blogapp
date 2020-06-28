from django.urls import path,include
from django.contrib.auth import urls
from accounts.views import UserCreateView,UpdateProfileView
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('signup/',UserCreateView.as_view(),name = 'signup'),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('profile/<slug:id>/',UpdateProfileView.as_view(),name = 'profile'),
    path('password-reset/',PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html'),name = 'password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name = 'accounts/password_confirm.html'),name = 'password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'),name = 'password_reset_complete'),
    path('password-change/',PasswordChangeView.as_view(template_name = 'accounts/password_change.html'),name = 'password_change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'),name = 'password_change_done'),
]