from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})

