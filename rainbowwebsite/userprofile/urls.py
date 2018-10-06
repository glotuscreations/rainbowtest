from django.urls import path, re_path
from userprofile import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'userprofile'

urlpatterns = [

    path('new/', views.NewUserProfileView.as_view(), name = 'newprofile'),
    path('users/<int:pk>/edit/', views.EditUserProfileView.as_view(), name="editprofile"),
    path('search/', views.profiles_list, name="profilesearch"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.profile_details, name="profileview"),
    re_path(r'^del/(?P<slug>\w+)/$', views.UserProfileDelete.as_view(), name="deleteprofile"),
    re_path(r'^report/(?P<slug>\w+)/$', views.contact, name="report"),
    


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
