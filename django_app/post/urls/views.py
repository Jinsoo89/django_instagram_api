from django.conf.urls import url

from .. import views

urlpatterns = [
    url(r'^post-list/$', views.post_list, name='post-list'),
    url(r'^create/$', views.post_create, name='post-create'),
    url(r'^photo/add/$', views.post_photo_add, name='photo_add'),
]
