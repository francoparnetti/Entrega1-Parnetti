from django.shortcuts import render, redirect
from .forms import CreateBlog, BlogSearch
from .models import Blog
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

login_required
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




class BlogDetail(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    
class BlogEdit(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog/blog_edit.html"
    success_url = "/blog/feed/"
    fields = ["title", "subtitle"]

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"
    success_url = "/blog/feed/"