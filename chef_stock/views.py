from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import Http404
import chef

from chef_stock.utils import ChefQueryManager

api = chef.autoconfigure()

def roles(request):
    request.breadcrumbs("Roles","#")
    roles = ChefQueryManager.list_roles()
    return render_to_response("roles.html",{'roles':roles},RequestContext(request))

def role(request,role_name):
    request.breadcrumbs("Roles",reverse("roles"))
    request.breadcrumbs(role_name,"#")
    role = ChefQueryManager.get_role(role_name)
    if not role:
        raise Http404
    return render_to_response("role.html",{'role':role},RequestContext(request))

def databags(request):
    request.breadcrumbs("DataBags","#")
    databags = ChefQueryManager.list_databags()
    return render_to_response("databags.html",{'databags':databags},RequestContext(request))

def databag(request,databag_name):
    request.breadcrumbs("DataBags",reverse("databags"))
    request.breadcrumbs(databag_name,"#")
    databag = ChefQueryManager.get_databag(databag_name)
    if not databag:
        raise Http404
    return render_to_response("databag.html",{'databag':databag},RequestContext(request))

def nodes(request):
    request.breadcrumbs("Nodes","#")

    cur_environment = request.GET.get("cur_environment",None)
    cur_role = request.GET.get("cur_role",None)
    cur_name = request.GET.get("cur_name",None)

    nodes = ChefQueryManager.list_nodes()
    if cur_environment or cur_role or cur_name:
        chef_map = dict([(node_name,ChefQueryManager.get_node(node_name)) for node_name in nodes])


    if cur_name:
        nodes = filter(lambda x: chef_map.get(x,None) and cur_name in chef_map.get(x)['name'],nodes)
    if cur_environment:
        nodes = filter(lambda x: chef_map.get(x,None) and chef_map.get(x)['chef_environment'] == cur_environment,nodes)
    if cur_role:
        nodes = filter(lambda x: chef_map.get(x,None) and chef_map.get(x)['automatic'].has_key("roles") and cur_role in chef_map.get(x)['automatic']['roles'],nodes)

    return render_to_response("nodes.html",
                              {'nodes':nodes,
                               'cur_name':cur_name,
                               'cur_role':cur_role,
                               'cur_environment':cur_environment},
                              RequestContext(request))

def node(request,node_name):    
    request.breadcrumbs("Nodes",reverse("nodes"))
    request.breadcrumbs(node_name,"#")
    node = ChefQueryManager.get_node(node_name)
    if not node:
        raise Http404
    return render_to_response("node.html",{'node':node},RequestContext(request))
