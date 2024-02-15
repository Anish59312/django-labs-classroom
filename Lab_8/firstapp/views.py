# blog/views.py
from django.shortcuts import render, redirect
from .models import Blog,BlogPost
from .forms import BlogForm
from django.contrib.auth.models import User

def home(request):
    blogs = Blog.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'blogs': blogs, 'blog_posts': blog_posts})

def blog(request):
    if request.method == "POST":
        print("method post for blog")
        form = BlogForm(request.POST)
        if form.is_valid():
            Blog.objects.create(
                blog_title = form.cleaned_data['title'],
                user = User.objects.get(username='anish')
            )
        return render(request, 'home.html')
    else:
        print("non post method call for blog")
        form = BlogForm()
        return render(request, 'blog.html', {'form' : form} )
    