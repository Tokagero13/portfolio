from projects.models import *

#Menu currently not in use
menu = [
    {'title': 'home', 'url_name': 'home'},
    {'title': 'profile', 'url_name': 'cv'},
    {'title': 'projects', 'url_name': 'projects'},
    {'title': 'login', 'url_name': 'login'}
    ]

projects = Project.objects.order_by('title').all()
project_img = ProjectImage.objects.all()

context = {
    'projects': projects,
    'menu': menu
}