# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from .models import CategoryPost


class PostListMixin(object):

        def get_context_data(self, **kwargs):
                context = super(PostListMixin, self).get_context_data(**kwargs)
                return context


class PostDetailMixin(object):

        def get_queryset(self):
                queryset = super(PostDetailMixin, self).get_queryset()
                slug = self.request.GET.get('slug')
                if slug:
                        return queryset.get_object_or_404(slug=slug)
                return queryset

        def get_context_data(self, **kwargs):
                context = super(PostDetailMixin,
                                self).get_context_data(**kwargs)
                context['entry'] = self.object
                return context


class SearchMixin(object):

        def get_queryset(self):
                queryset = super(SearchMixin, self).get_queryset()
                slug = self.request.GET.get('slug')
                if slug:
                        return queryset.get_list_or_404(category__slug=slug)
                return queryset

        def get_context_data(self, **kwargs):
                context = super(SearchMixin, self).get_context_data(**kwargs)
                _slug = self.kwargs.get('slug')
                category = get_object_or_404(CategoryPost, slug=_slug)
                context['post'] = self.object_list
                context['category'] = category
                return context
