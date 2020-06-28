from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
from blog.forms import ContactForm,PostForm,Search
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from accounts.models import User


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = 'posts'
    queryset = Post.objects.filter(status = "P")
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        form = Search()
        posts = Post.objects.filter(status = "P")
        category = Category.objects.all()
        return render(request,'blog/index.html',context={'form':form,'category':category,'posts':posts})


    def post(self, request, *args, **kwargs):
        form = Search(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            posts = Post.objects.filter(title__contains = form.cleaned_data['search_blog'])
            category = Category.objects.all()
            return render(request,'blog/index.html',context={'form':form,'category':category,'posts':posts})
        return render(request,'blog/index.html',context={'form':form,'category':category,'posts':posts})
        

class CategoryIndexView(ListView):
    model = Post
    template_name = 'blog/category_index.html'
    context_object_name = 'category'
    queryset = Category.objects.all()

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        categoryobj = Category.objects.get(slug = self.kwargs['slug'])
        posts = Post.objects.filter(category = categoryobj)
        context['posts'] = posts
        return context


class BlogDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'
 

class ContactFormView(FormView):
    form_class = ContactForm
    success_url = 'contactus'
    template_name = 'blog/contact.html'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PostModelFormView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'login'
    permission_required = 'blog.add_post'
    template_name =  'blog/post.html'
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostFormUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url ='login'
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostForm
    template_name = 'blog/post.html'

    def test_func(self,*args,**kwargs):
        author = Post.objects.get(slug=self.kwargs['slug']).author
        return author == self.request.user



class PostDeleteView(PermissionRequiredMixin,UserPassesTestMixin,DeleteView):
    permission_required ='blog.delete_post'
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/stories'

    def test_func(self,*args,**kwargs):
        author = Post.objects.get(slug=self.kwargs['slug']).author
        return author == self.request.user



        



