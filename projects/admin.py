from django.contrib import admin
from .models import Project, ProjectImage
from .models import CV, PersonalInfo, Education, Experience, Skill, Project

# my CV
class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class CVAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline, SkillInline, ProjectInline]

admin.site.register(PersonalInfo)
admin.site.register(CV, CVAdmin)

# Projects
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    verbose_name = 'Add image to poject'
    verbose_name_plural = 'Add image to poject'
    extra = 1  # Number of extra forms to display
    list_display = ('project', 'image')
    search_fields = ('project', 'image')

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'technology')
    search_fields = ('title', 'technology')

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'project_id')
    searach_fields = ('image', 'project_id')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

