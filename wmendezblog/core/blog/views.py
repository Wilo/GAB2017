from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.http import Http404

from .mixins import BlogMixin, PostMixin
from .models import Post, CategoriaPost


class BlogListView(BlogMixin, ListView):

    model = Post
    template_name = "index.html"


class BlogDetailView(PostMixin, DetailView):

    model = Post
    template_name = "blog.html"


class SearchPostView(View):

    template_name = "search.html"

    def get(self, request, **kwargs):
        try:
            post = Post.objects.filter(categoria__slug=kwargs['slug'])
            category = CategoriaPost.objects.get(slug=kwargs['slug'])
            context = {'post': post, 'category': category}

            return render(request, self.template_name, context)
        except Exception:
            raise Http404
