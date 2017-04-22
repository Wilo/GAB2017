from django.conf.urls import url
from .views import BlogListView, BlogDetailView, SearchPostView
from .rss import BlogFeed

urlpatterns = [
                url(r'^$', BlogListView.as_view(), name="Entrada Blog"),
                url(r'^post/(?P<slug>[-\w]+)$', BlogDetailView.as_view(),
                    name="entrada"),
                url(r'^search/(?P<slug>[-\w]+)$', SearchPostView.as_view(),
                    name="buscar"),
                url(r'^feed/$', BlogFeed(), name="Rss Channel"),
]
