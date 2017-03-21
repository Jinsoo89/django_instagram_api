from django.conf.urls import url

from .. import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(),
        name='post-delete'),
    url(r'^create/$', views.PostCreate.as_view(), name='post-create'),
    url(r'^(?P<post_pk>[0-9]+)/comment/create/$',
        views.CommentCreate.as_view(),
        name='comment-create'),
    # url(r'^post-list/$', views.post_list, name='post-list'),
    # url(r'^create/$', views.post_create, name='post-create'),
    # url(r'^photo/add/$', views.post_photo_add, name='photo_add'),
]
