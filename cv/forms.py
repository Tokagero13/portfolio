from django import forms
from django.forms import inlineformset_factory
from .models import CV, PersonalInfo, Education, Experience, Skill, CVProject


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['summary', 'personal_info']

EducationFormSet = inlineformset_factory(CV, Education, fields=['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'description'], extra=1)
ExperienceFormSet = inlineformset_factory(CV, Experience, fields=['job_title', 'company', 'start_date', 'end_date', 'description'], extra=1)
SkillFormSet = inlineformset_factory(CV, Skill, fields=['name', 'proficiency'], extra=1)
CVProjectFormSet = inlineformset_factory(CV, CVProject, fields=['title', 'description', 'technology', 'image'], extra=1)
