from django.conf.urls import patterns, include, url

urlpatterns = patterns('chef_stock.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^roles/$','roles',name='roles'),
                       url(r'^roles/(?P<role_name>.*)/$','role',name='roles'),
                       url(r'^nodes/$','nodes',name='nodes'),
                       url(r'^nodes/(?P<node_name>.*)/$','node',name='node'),
                       url(r'^databags/$','databags',name='databags'),
                       url(r'^databags/(?P<databag_name>.*)/$','databag',name='databag'),
                       
                       
                       
)
