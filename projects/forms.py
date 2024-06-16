from django import forms
from .models import Project, ProjectImage
from django.forms.models import inlineformset_factory

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology']

ProjectImageFormSet = inlineformset_factory(Project, ProjectImage, fields=['image'], extra=5, max_num=5)
