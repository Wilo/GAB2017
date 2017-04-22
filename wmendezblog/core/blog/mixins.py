

class BlogMixin(object):

        def get_context_data(self, **kwargs):
                context = super(BlogMixin, self).get_context_data(**kwargs)
                return context


class PostMixin(object):

        def get_queryset(self):
                queryset = super(PostMixin, self).get_queryset()
                slug = self.request.GET.get('slug')
                if slug:
                        return queryset.get(slug=slug)
                return queryset

        def get_context_data(self, **kwargs):
                context = super(PostMixin, self).get_context_data(**kwargs)
                context['entrada'] = self.object
                return context


class SearchMixin(object):

        def get_queryset(self):
                queryset = super(SearchMixin, self).get_queryset()
                slug = self.request.GET.get('slug')
                if slug:
                        return self.request.GET.filter(categoria__slug=slug)
                return queryset
