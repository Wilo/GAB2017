# -*- coding: utf-8 -*-
from textwrap import shorten
from os.path import splitext
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed

from .models import Post


class RssBlogFeed(Feed):

    title = "Last News"
    link = "/news/rss"
    description = "Free/Opensource Web Developer"

    def items(self):
        return Post.objects.order_by('-date_creation')

    def item_author_name(self, item):
        return item.user.username

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_creation

    def item_description(self, item):
        return shorten(item.description, width=250, placeholder=" ...")

    def item_link(self, item):
        return reverse('post', args=[item.slug])

    def item_enclosure_url(self, item):
        # FIXME obtain the full current url here
        return "http://localhost:8000{}".format(item.img_header.url)

    def item_enclosure_length(self, item):
        return item.post_length()

    def item_enclosure_mime_type(self, item):
        fileExtension = splitext(item.img_header.name)[1].split('.')[1]
        if fileExtension == 'jpg':
            fileExtension = 'jpeg'
        return "image/%s" % (fileExtension)


class AtomBlogFeed(RssBlogFeed):
    feedtype = Atom1Feed
    description = RssBlogFeed.description
