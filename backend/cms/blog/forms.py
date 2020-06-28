from django import forms
import re
from blog.models import Post
from tinymce.widgets import TinyMCE
from accounts.models import User

class ContactForm(forms.Form):

    countries = [('IND','INDIA'),('CHN','CHINA')]
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required = False)
    phone = forms.RegexField(regex='^[6-9][0-9]{9}$',required = False)
    message = forms.CharField(max_length=500,widget=forms.Textarea)
    country = forms.ChoiceField(choices=countries)


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if email == "" and phone == "":
            raise forms.ValidationError("atleast email or password should be provided")


class Search(forms.Form):
    search_blog = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'searchbar'}))

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'id':'title'}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 40,'id' :'content'}))

    class Meta:
        model = Post
        fields = ['title','content','date','author','status','category','images']

    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
