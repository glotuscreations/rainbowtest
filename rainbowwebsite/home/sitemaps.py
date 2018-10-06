from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home:index', 'home:about', 'home:signup', 'login']

    def location(self, item):
        return reverse(item)
