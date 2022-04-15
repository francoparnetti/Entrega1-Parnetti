from django.shortcuts import render, redirect
from .forms import CreateBlog, BlogSearch
from .models import Blog
# Create your views here.


def create_blog(request):
    if request.method == "POST":
        form = CreateBlog(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            blog = Blog(title=data["title"],subtitle=data["subtitle"])
            blog.save()
            return redirect("blog_feed")
    
    
    form = CreateBlog()
    return render(request, "blog/create_blog.html", {"form": form})

def blog_feed(request):
    
    blog_title =request.GET.get("title", None)
    
    if blog_title is not None:
        blogs = Blog.objects.filter(title__icontains=blog_title)
    else:
        blogs = Blog.objects.all()
    form = BlogSearch()
    return render(request, "blog/blog_feed.html", {"form": form, "blogs": blogs}) 