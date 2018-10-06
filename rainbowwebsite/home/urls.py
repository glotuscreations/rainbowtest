from django.urls import path, include
from home import views
from home.sitemaps import StaticSitemap
from django.contrib.sitemaps.views import sitemap

app_name = 'home'

sitemaps = {'static': StaticSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('', views.index, name = 'index'),
    path('about/', views.aboutus, name = 'about'),
    path('signup/',  views.SignUpFormView.as_view(), name = 'signup'),
    path('success/', views.success, name="success"),
    path('terms/', views.terms, name="terms"),

    ]
