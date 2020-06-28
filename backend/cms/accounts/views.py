from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from accounts.forms import SignUpForm,UpdateProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User


class UserCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = "login"


class UpdateProfileView(UpdateView):
    model = User
    pk_url_kwarg = 'id'
    form_class = UpdateProfileForm
    template_name = 'accounts/update_profile.html'
    success_url = "/stories"


    