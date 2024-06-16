from django import template
from projects.models import *

register = template.Library()

@register.simple_tag()
def get_prj_img(project_title):
    return ProjectImage.objects.filter(project=project_title)