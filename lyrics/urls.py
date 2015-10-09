from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.aching, name='aching'),
    url(r'^(?P<verse_id>[0-9]+)/$', views.verse_view, name='verse_view'),
]
