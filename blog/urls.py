from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("blog/",views.blog_list,name="all_blog"),
    path("blog/create",views.blog_create,name="blog_create"),
    path("blog/<int:blog_id>/delete",views.blog_delete,name="blog_delete"),
    path("blog/<int:blog_id>/edit",views.blog_edit,name="blog_edit"),
    path("blog/<slug:slug>",views.blog_details,name="blog_detail"),
    path("register/",views.registration,name="register"),
    ]
