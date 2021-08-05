from django.shortcuts import render
from blog.models import Categoria, Post
# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,'blog/blog.html', {'posts':post})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias=categoria)
    return render(request, 'blog/categorias.html', {'categorias':categoria, 'posts':post})