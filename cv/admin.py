from django.contrib import admin
from .models import CV, PersonalInfo, Education, Experience, Skill, CVProject

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

admin.site.register(PersonalInfo)
admin.site.register(CV, CVAdmin)
