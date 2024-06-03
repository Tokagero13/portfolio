from django.shortcuts import render
from .models import Project
from django.views.generic.detail import DetailView
from django.http import HttpResponse

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

def CV(request):
    return render(request, 'projects/my_cv.html')