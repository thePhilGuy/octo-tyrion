from django.conf.urls import patterns, url
from mini_url.views import URLCreate, URLUpdate, MiniList

urlpatterns = patterns('mini_url.views',
    url(r'^new_link/$', URLCreate.as_view(), name="new_link"),
    url(r'^home/$', MiniList.as_view(), name="Mini_home"),
    url(r'^(?P<short_url>\w{10})/$', 'target', name="target"),
    url(r'^edit/(?P<short_url>\w{10})/$', URLUpdate.as_view(), name="edit_link")
)
