# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .mixins import PostListMixin, PostDetailMixin, SearchMixin
from .models import Post


class BlogListView(PostListMixin, ListView):

    model = Post
    template_name = "index.html"


class BlogDetailView(PostDetailMixin, DetailView):

    model = Post
    template_name = "blog.html"


class SearchPostView(SearchMixin, ListView):

    model = Post
    template_name = "search.html"
