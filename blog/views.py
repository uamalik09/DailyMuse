from django.shortcuts import render
from .models import Blog
from .forms import BlogForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def home(request):
    latest_blog=Blog.objects.all().order_by("-created_at")[:3]
    return render(request,'home.html',{
        "latest_blog":latest_blog
    })


def blog_list(request):
    all_blogs=Blog.objects.all().order_by("-created_at")
    return render(request,'all_blog.html',{
        "all_blogs":all_blogs
        })


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('all_blog')
        
    else:
        form = BlogForm()
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_edit(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('all_blog')
        
    else:
        form = BlogForm(instance=blog)
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_delete(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('all_blog')
    return render(request,'blog_delete.html',{'blog':blog})

def blog_details(request,slug):
    identified_blog=get_object_or_404(Blog, slug=slug)
    return render(request,"blog_detail.html",{
        "blog":identified_blog
    })

def registration(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid:
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('home') 
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})