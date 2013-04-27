from django import template
register = template.Library()

def magical_template(value):
    if isinstance(value,dict):
        output =  pretty_dict(value)
    else:
        output = value

    return output


def pretty_dict(d):
    output_template = "<ul>%s</ul>"
    output = ""
    for key,value in d.items():
        if isinstance(value,dict):
            output+="<li><a href='#' class='expander'>%s</a>: <div class='hide'>%s</div></li>" % (key,pretty_dict(value))
        else:
            output+="<li>%s: %s</li>" % (key,value)
            
    return output_template % output
    

register.filter('magical_template', magical_template)
