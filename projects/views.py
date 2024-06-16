from django.shortcuts import render, redirect
from .models import *
from django.views.generic.detail import DetailView
from django.http import HttpResponse


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
