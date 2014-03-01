from django.conf.urls import patterns, url

from electoral_data import views

urlpatterns = patterns('',
	# ex: /view/
    url(r'^$', views.index, name='index'),
    # ex: /view/ls
    url(r'^ls/$', views.ls, name='loksabha'),
    # ex: /view/assembly/5
    url(r'^assembly/(?P<ls_id>\d+)/$', views.assembly, name='assembly'),
    # ex: /view/polling/31
    url(r'^polling/(?P<assembly_id>\w+)/$', views.polling, name='polling'),
     # ex: /view/part/31
    url(r'^part/(?P<polling_station_id>\w+)/$', views.part, name='part'),
    # ex: /view/citizens/192
    url(r'^citizens/(?P<part_no>\w+)/$', views.citizens, name='citizens'),
    # ex: /view/detail/192
    url(r'^detail/(?P<citizen_id>\d+)/$', views.detail, name='detail'),
)