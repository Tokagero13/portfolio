from django.contrib import admin
from .models import CV, PersonalInfo, Education, Experience, Skill, CVProject, Messages

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

class MessagesAdmin(admin.ModelAdmin):
    model = Messages
    verbose_name = 'Messages from Contact us form'
    verbose_name_plural = 'Messages from Contact us form'
    list_display = ('user', 'contact_us_msg', 'time_created')
    search_fields = ('user', 'time_created')

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
admin.site.register(Messages, MessagesAdmin)
