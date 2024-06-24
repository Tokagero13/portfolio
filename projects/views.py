from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic.detail import DetailView

#Main variables
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

# Create your views here.
def index(request):
    return render(request, 'projects/index.html', context = context)

def auth(request):
    return render(request, 'projects/auth.html', context=context)

def CV_view(request):
    return render(request, 'projects/cv.html', context=context)

def AllProjects(request):
    return render(request, 'projects/all_projects.html', {
        'projects': projects,
        'project_img': project_img
        }
    )

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'project_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        # Fetch images related to this project
        context['project_img'] = self.object.images.all()
        return context
