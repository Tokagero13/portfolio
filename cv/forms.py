from django import forms
from django.forms import inlineformset_factory
from .models import CV, PersonalInfo, Education, Experience, Skill, CVProject, Messages

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['first_name','last_name','email', 'phone']
    
#----------------------------------------------
Contact_us_extraFormSet = inlineformset_factory(PersonalInfo, Messages, fields=['Contact_us_msg'], extra=1)

# class ContactUs_extraForm(forms.Form):
#     message = forms.CharField(label='Message', widget=forms.Textarea)
#     METHODS = [
#         ('whatsapp', 'WhatsApp'),
#         ('telegram', 'Telegram'),
#         ('email', 'Email'),
#         ('phone_call', 'Phone call'),
#         ('any', 'Any'),
#     ]
#     contact_method = forms.ChoiceField(choices=METHODS, label='Contact Method', initial=True, required=True)

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
