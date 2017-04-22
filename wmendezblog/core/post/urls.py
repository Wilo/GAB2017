from django.conf.urls import url
from .views import BlogListView, BlogDetailView, SearchPostView
from .rss import RssBlogFeed, AtomBlogFeed

urlpatterns = [
                url(r'^$', BlogListView.as_view(), name="entry"),
                url(r'^post/(?P<slug>[-\w]+)$', BlogDetailView.as_view(),
                    name="post"),
                url(r'^search/(?P<slug>[-\w]+)$', SearchPostView.as_view(),
                    name="search"),
                url(r'^news/rss$', RssBlogFeed(), name="Rss Channel"),
                url(r'^news/atom$', AtomBlogFeed(), name="Atom Channel")
]
