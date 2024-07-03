from cv.models import CVProject, Education, Experience, PersonalInfo, Skill
from projects.models import *

#Main variables
menu = [
    {'title': 'home', 'url_name': 'home'},
    {'title': 'profile', 'url_name': 'cv'},
    {'title': 'projects', 'url_name': 'projects'},
    {'title': 'login', 'url_name': 'login'}
    ]

projects = Project.objects.order_by('title').all()
project_img = ProjectImage.objects.all()

# Initialize cv_project dictionary
cv_project = {
    'Personal Info': PersonalInfo.objects.all(),
    'Experience': Experience.objects.all(),
    'Education': Education.objects.all(),
    'Projects': CVProject.objects.all(),
    'Skills': Skill.objects.all(),
}

# Define your list of models
models_list = [CVProject, Skill, Experience, Education, PersonalInfo]

# Initialize empty list to collect all field names
experience_fields = []

# Iterate over each model to fetch field names
for model in models_list:
    model_fields = [field.name for field in model._meta.get_fields() if field.name != 'id']
    experience_fields.extend(model_fields)

# Remove duplicates and maintain order (if necessary)
experience_fields = list(dict.fromkeys(experience_fields))

context = {
    'cv_project': cv_project,
    'experience_fields': experience_fields,
    'projects': projects,
    'menu': menu
}