from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
import chef

from chef_stock.utils import ChefQueryManager

api = chef.autoconfigure()

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def roles(request):
    roles = ChefQueryManager.list_roles()
    return render_to_response("roles.html",{'roles':roles},RequestContext(request))

def role(request,role_name):
    role = ChefQueryManager.get_role(role_name)
    if not role:
        raise Http404
    return render_to_response("role.html",{'role':role},RequestContext(request))

def databags(request):
    databags = ChefQueryManager.list_databags()
    return render_to_response("databags.html",{'databags':databags},RequestContext(request))

def databag(request,databag_name):
    databag = ChefQueryManager.get_databag(databag_name)
    if not databag:
        raise Http404
    return render_to_response("databag.html",{'databag':databag},RequestContext(request))

def nodes(request):
    nodes = ChefQueryManager.list_nodes()
    return render_to_response("nodes.html",{'nodes':nodes},RequestContext(request))

def node(request,node_name):    
    node = ChefQueryManager.get_node(node_name)
    if not node:
        raise Http404
    return render_to_response("node.html",{'node':node},RequestContext(request))
