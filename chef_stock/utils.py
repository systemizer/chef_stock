from django.core.cache import cache
import chef
import json

api = chef.autoconfigure()

CACHE_TIMEOUT = 60*60

class ChefQueryManager(object):
    _node_key = "NODE:::%s"
    _role_key = "ROLE:::%s"
    _databag_key = "DATABAG:::%s"
    _nodes_list_key = "NODES"
    _databags_list_key = "DATABAGS"
    _roles_list_key = "ROLES"

    @classmethod
    def get_node(cls,node_name):
        if not cache.has_key(cls._node_key % node_name):
            node = chef.Node(node_name,api=api)
            if not node.exists:
                return None
            cache.set(cls._node_key % node_name,json.dumps(node.to_dict()),CACHE_TIMEOUT)

        return json.loads(cache.get(cls._node_key % node_name))

    @classmethod
    def get_databag(cls,databag_name):
        if not cache.has_key(cls._databag_key % databag_name):
            databag = chef.DataBag(databag_name,api=api)
            if not databag.exists:
                return None
            cache.set(cls._databag_key % databag_name,json.dumps(databag.to_dict()),CACHE_TIMEOUT)

        return json.loads(cache.get(cls._databag_key % databag_name))

    @classmethod
    def get_role(cls,role_name):
        if not cache.has_key(cls._role_key % role_name):
            role = chef.Role(role_name,api=api)
            if not role.exists:
                return None
            cache.set(cls._role_key % role_name,json.dumps(role.to_dict()),CACHE_TIMEOUT)

        return json.loads(cache.get(cls._role_key % role_name))

    @classmethod
    def list_nodes(cls):
        if not cache.has_key(cls._nodes_list_key):
            nodes = list(chef.Node.list(api=api))
            cache.set(cls._nodes_list_key,json.dumps(nodes),CACHE_TIMEOUT)

        return json.loads(cache.get(cls._nodes_list_key))

    @classmethod
    def list_roles(cls):
        if not cache.has_key(cls._roles_list_key):
            roles = list(chef.Role.list(api=api))
            cache.set(cls._roles_list_key,json.dumps(roles),CACHE_TIMEOUT)

        return json.loads(cache.get(cls._roles_list_key))
            
    @classmethod
    def list_databags(cls):
        if not cache.has_key(cls._databags_list_key):
            databags = list(chef.DataBag.list(api=api))
            cache.set(cls._databags_list_key,json.dumps(databags),CACHE_TIMEOUT)

        return json.loads(cache.get(cls._databags_list_key))
