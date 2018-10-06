from django.contrib.sitemaps import Sitemap
from posts.models import Post


class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
