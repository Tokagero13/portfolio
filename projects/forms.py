from django import forms
from .models import *
from django.forms import inlineformset_factory


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology']

ProjectImageFormSet = inlineformset_factory(Project, ProjectImage, 
                                                fields=['image'], 
                                                extra=1, 
                                                max_num=5,
                                            )