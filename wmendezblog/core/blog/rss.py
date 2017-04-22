# -*- coding: utf-8 -*-
from os.path import splitext
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Post, CategoriaPost


class BlogFeed(Feed):
    title = "In.planet"
    link  = "/rss/"
    description = "In.planet, Más que internet"

    def items(self):
        return Post.objects.order_by('-fech_crea')

    def item_title(self, item):
        return item.titulo

    def item_pubdate(self, item):
        return item.fech_crea

    def item_description(self, item):
        return item.descripcion

    def item_link(self, item):
        return reverse('entrada', args=[item.slug])
