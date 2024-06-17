# your_app/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(obj, attr_name):
    try:
        value = getattr(obj, attr_name)
        if attr_name == 'id' or value is None or value == '':
            return None  # Return None to indicate empty or ignored field
        return value
    except AttributeError:
        return None  # Return None if attribute does not exist
