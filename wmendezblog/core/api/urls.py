from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import CategoryPostViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryPostViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
