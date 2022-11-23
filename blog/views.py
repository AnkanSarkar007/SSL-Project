from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from venue.models import Hangout
import decimal
from django.template.defaulttags import register

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['venue', 'title', 'rating', 'content']
    
    def form_valid(self, form):
        s = form.instance.venue
        obj = Hangout.objects.get(pk = int(s[:s.find(':')]))
        obj.total += 1
        obj.rate += form.instance.rating
        obj.rating = obj.rate / obj.total
        obj.save()
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['venue', 'title', 'rating', 'content']
    
    def form_valid(self, form):
        s = form.instance.venue
        obj = Hangout.objects.get(pk = int(s[:s.find(':')]))
        obj.total += 1
        obj.rate += form.instance.rating
        obj.rating = obj.rate / obj.total
        obj.save()
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            s = post.venue
            obj = Hangout.objects.get(pk = int(s[:s.find(':')]))
            obj.rate -= decimal.Decimal(post.rating/2)
            obj.total -= decimal.Decimal(0.5)
            if obj.total != 0:
                obj.rating = obj.rate / obj.total
            else:
                obj.rating = 0
            obj.save()
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            s = post.venue
            obj = Hangout.objects.get(pk = int(s[:s.find(':')]))
            obj.rate -= decimal.Decimal(post.rating/2)
            obj.total -= decimal.Decimal(0.5)
            if obj.total != 0:
                obj.rating = obj.rate / obj.total
            else:
                obj.rating = 0
            obj.save()
            return True
        return False
    
@register.filter
def get_range(value):
    return range(value)
@register.filter
def get_range1(value):
    return range(5 - value)
@register.filter
def trim(value):
    return value[value.find(':')+1:]
@register.filter
def pre_trim(value):
    return value[:value.find(':')]