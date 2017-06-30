from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #   /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register$', views.UserFormView.as_view(), name='register'),
#   /music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    #music/album/id
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # music/album/id/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

]


# urlpatterns = [
#     #   /music/
#     url(r'^$', views.index, name='index'),
# #   /music/album_id/
#     url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
# #   /music/album_id/favorite
#     url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),
# ]
