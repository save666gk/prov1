from django.views.generic import ListView, DetailView
from .models import Post
class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/post.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'post'

class PostDetail(DetailView):
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'flatpages/postpk.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'