from django import forms
from django.forms import inlineformset_factory
from .models import CV, PersonalInfo, Education, Experience, Skill, CVProject, Messages

# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = PersonalInfo
#         fields = ['first_name','last_name','email', 'phone']
    
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['first_name', 'last_name', 'email', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        
        if email:
            existing_user = PersonalInfo.objects.filter(email=email).first()
            if existing_user:
                self.instance = existing_user  # Assign existing user to form instance
            else:
                self.instance = None  # No existing user found, form will save a new instance
        
        return cleaned_data

Contact_us_extraFormSet = inlineformset_factory(PersonalInfo, Messages, fields=['contact_us_msg'], extra=1)

class ContactUs_extraForm(forms.Form):
    message = forms.CharField(label='Message', widget=forms.Textarea, required=False)
    METHODS = [
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('email', 'Email'),
        ('phone_call', 'Phone call'),
        ('any', 'Any'),
    ]
    contact_method = forms.ChoiceField(choices=METHODS, label='Contact Method', initial='any')

"""Class below can be used insted of ContactUs_extraForm (go to cv/views.py change variable extra_form -uncomment-)"""
class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['contact_us_msg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally customize form field widgets or add additional logic

    def clean_user(self):
        user = self.cleaned_data['user']
        # Validate if the user selected exists in the PersonalInfo model
        if not PersonalInfo.objects.filter(pk=user.pk).exists():
            raise forms.ValidationError('Invalid user selected.')
        return user

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
