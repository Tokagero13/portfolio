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

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['summary', 'personal_info']

EducationFormSet = inlineformset_factory(CV, Education, 
                                         fields=['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'description'], 
                                         extra=1
                                         )
ExperienceFormSet = inlineformset_factory(CV, Experience, 
                                          fields=['job_title', 'company', 'start_date', 'end_date', 'description'], 
                                          extra=1
                                          )
SkillFormSet = inlineformset_factory(CV, Skill, 
                                     fields=['name', 'proficiency'], 
                                     extra=1
                                     )
ProjectFormSet = inlineformset_factory(CV, Project, 
                                       fields=['title', 'description', 'technology', 'image'], 
                                       extra=1
                                       )
