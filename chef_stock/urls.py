from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('chef_stock.views',
                       url(r'^$', 'nodes', name='nodes'),
                       url(r'^roles/$','roles',name='roles'),
                       url(r'^roles/(?P<role_name>.*)/$','role',name='role'),
                       url(r'^nodes/(?P<node_name>.*)/$','node',name='node'),
                       url(r'^databags/$','databags',name='databags'),
                       url(r'^databags/(?P<databag_name>.*)/$','databag',name='databag'),
                       
                       
                       
)

urlpatterns += staticfiles_urlpatterns()
