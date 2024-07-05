from winreg import CreateKey
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import View

from django.contrib.auth import login, logout

from projects.forms import RegisterUserForm
from .models import *

from django.views.generic.detail import DetailView

from django.core.paginator import Paginator
from projects.utils import *

class AuthView(View):
    template_name = 'projects/auth.html'

    def get(self, request, *args, **kwargs):
        register_form = RegisterUserForm()
        login_form = AuthenticationForm()
        context['register_form'] = register_form
        context['login_form'] = login_form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'register' in request.POST:
            register_form = RegisterUserForm(request.POST)
            login_form = AuthenticationForm()
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            register_form = RegisterUserForm()
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
        else:
            register_form = RegisterUserForm()
            login_form = AuthenticationForm()
        
        context['register_form'] = register_form
        context['login_form'] = login_form
        return render(request, self.template_name, context)

def technologies(request):
    return render(request, 'projects/technologies.html', context=context)

def logout_user(request):
    logout(request)
    return redirect('auth')

def index(request):
    return render(request, 'projects/index.html', context=context)

def auth(request):
    return render(request, 'projects/auth.html', context=context)

def CV_view(request):
    return render(request, 'projects/cv.html', context=context)

def AllProjects(request):
    context['project_img'] = project_img
    paginator = Paginator(projects, 3)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'projects/all_projects.html', context=context
    )

class ProjectDetailView(DetailView):
    paginate_by = 3
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'project_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_img'] = self.object.images.all()
        return context


#___REST API___
from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    #A viewset for viewing and editing user instances.

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
