from django.shortcuts import render, redirect
from .models import *
from .forms import CVForm, PersonalInfoForm, EducationFormSet, ExperienceFormSet, SkillFormSet, CVProjectFormSet
from projects.views import Project

#Main variables
menu = [
    {'title': 'home', 'url_name': 'home'},
    {'title': 'profile', 'url_name': 'cv'},
    {'title': 'projects', 'url_name': 'projects'},
    {'title': 'login', 'url_name': 'login'}
    ]

projects = Project.objects.order_by('title').all()
# project_img = ProjectImage.objects.all()


# Initialize cv_project dictionary
cv_project = {
    'CVs': CV.objects.all(),
    'Projects': CVProject.objects.all(),
    'Skills': Skill.objects.all(),
    'Experience': Experience.objects.all(),
    'Education': Education.objects.all(),
    'Personal Info': PersonalInfo.objects.all()
}

# Define your list of models
models_list = [CV, CVProject, Skill, Experience, Education, PersonalInfo]

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

# Create your views here.
def index(request):
    return render(request, 'cv/index.html', context=context)


def create_cv(request):
    if request.method == "POST":
        personal_info_form = PersonalInfoForm(request.POST)
        if personal_info_form.is_valid():
            personal_info = personal_info_form.save()
            cv_form = CVForm(request.POST, instance=CV(personal_info=personal_info))
            if cv_form.is_valid():
                cv = cv_form.save()
                education_formset = EducationFormSet(request.POST, instance=cv)
                experience_formset = ExperienceFormSet(request.POST, instance=cv)
                skill_formset = SkillFormSet(request.POST, instance=cv)
                cv_project_formset = CVProjectFormSet(request.POST, request.FILES, instance=cv)
                
                if all([education_formset.is_valid(), experience_formset.is_valid(), skill_formset.is_valid(), cv_project_formset.is_valid()]):
                    education_formset.save()
                    experience_formset.save()
                    skill_formset.save()
                    cv_project_formset.save()
                    return redirect('cv/cv_django.html', pk=cv.pk)
    else:
        personal_info_form = PersonalInfoForm()
        cv_form = CVForm()
        education_formset = EducationFormSet()
        experience_formset = ExperienceFormSet()
        skill_formset = SkillFormSet()
        cv_project_formset = CVProjectFormSet()

    return render(request, 'cv/create_cv.html', {
        'personal_info_form': personal_info_form,
        'cv_form': cv_form,
        'education_formset': education_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'cv_project_formset': cv_project_formset,
    })

def cv_detail(request):
    return render(request, 'cv/cv_django.html', context=context)

def cv_html(request):
    return render(request, 'cv/cv_html.html', context=context)