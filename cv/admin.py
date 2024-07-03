from django.contrib import admin
from .models import CV, ContactUs, PersonalInfo, Education, Experience, Skill, CVProject

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class CVProjectInline(admin.TabularInline):
    model = CVProject
    extra = 1

class CVAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline, SkillInline, CVProjectInline]

class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    verbose_name = 'Contact Us'
    verbose_name_plural = 'Contact Us'
    readonly_fields = ['full_name', 'email', 'phone', 'methods', 'message', 'time_created']
    list_display = ('full_name', 'phone', 'methods', 'time_created')
    search_fields = ('full_name', 'email', 'phone', 'methods', 'time_created')

class PersonalInfoAdmin(admin.ModelAdmin):
    model = PersonalInfo
    verbose_name = 'Personal info'
    verbose_name_plural = 'Personal info'
    list_display = ('full_name', 'phone', 'email')  # Include 'full_name' in list_display
    search_fields = ('first_name', 'last_name', 'phone', 'email')

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"  # Define a method to return full name

    full_name.short_description = 'Full Name'  # Set a short description for the column

admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
