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
    # ex: /view/socities/42
    url(r'^societies/(?P<polling_id>\d+)/$', views.societies, name='societies'),
    # ex: /view/citizens/192
    url(r'^citizens/(?P<society_id>\w+)/$', views.citizens, name='citizens'),
    # ex: /view/detail/192
    url(r'^detail/(?P<citizen_id>\d+)/$', views.detail, name='detail'),
)