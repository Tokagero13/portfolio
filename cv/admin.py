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
    search_fields = ('user')

admin.site.register(PersonalInfo)
admin.site.register(CV, CVAdmin)
admin.site.register(Messages)
