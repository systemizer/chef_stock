from chef_stock.utils import ChefQueryManager

def chef_stock(request):
    return {
        "ENVIRONMENTS" : ChefQueryManager.list_environments(),
        "ROLES" : ChefQueryManager.list_roles()
        }
    
