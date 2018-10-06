from django.urls import path, re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from posts.sitemaps import PostSitemap

app_name = 'posts'

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('', views.postshome, name='postshome'),
    path('create/', views.post_new, name='create'),
    re_path(r'^del/(?P<pk>\w+)/$', views.PostDelete.as_view(), name="deletepost"),
]
