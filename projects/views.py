from django.shortcuts import render, redirect
from .models import *
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .forms import CVForm, PersonalInfoForm, EducationFormSet, ExperienceFormSet, SkillFormSet, ProjectFormSet

#Main variables
menu = [
    {'title': 'home', 'url_name': 'home'},
    {'title': 'profile', 'url_name': 'cv'},
    {'title': 'projects', 'url_name': 'projects'},
    {'title': 'login', 'url_name': 'login'}
    ]
projects = Project.objects.order_by('title').all()
project_img = ProjectImage.objects.all()

# Create your views here.
def index(request):
    context = {
        'projects': projects,
        'menu': menu
    }
    return render(request, 'projects/index.html', context = context)

def CV_view(request):
    my_cv = CV.objects.all()
    return render(request, 'projects/cv.html', {
        'CV': my_cv,
        'projects': projects
        })

def AllProjects(request):
    return render(request, 'projects/all_projects.html', {
        'projects': projects,
        'project_img': project_img
    })

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        # Fetch images related to this project
        context['project_img'] = self.object.images.all()
        return context
    
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
                project_formset = ProjectFormSet(request.POST, request.FILES, instance=cv)
                
                if all([education_formset.is_valid(), experience_formset.is_valid(), skill_formset.is_valid(), project_formset.is_valid()]):
                    education_formset.save()
                    experience_formset.save()
                    skill_formset.save()
                    project_formset.save()
                    return redirect('cv_detail', pk=cv.pk)
    else:
        personal_info_form = PersonalInfoForm()
        cv_form = CVForm()
        education_formset = EducationFormSet()
        experience_formset = ExperienceFormSet()
        skill_formset = SkillFormSet()
        project_formset = ProjectFormSet()

    return render(request, 'create_cv.html', {
        'personal_info_form': personal_info_form,
        'cv_form': cv_form,
        'education_formset': education_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset,
    })

def cv_detail(request, pk):
    cv = CV.objects.get(pk=pk)
    return render(request, 'cv_detail.html', {'cv': cv})