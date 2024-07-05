from datetime import datetime
import os
from django.db import models
from django.urls import reverse

def project_image_upload_to(instance, filename):
    # This function will return the path where the image should be uploaded
    # Get the file extension
    ext = filename.split('.')[-1]
    
    # Create a unique filename using the current timestamp
    unique_filename = f"{datetime.now().strftime('%Y-%m-%d/%H-%M-%S-%f')}.{ext}"
    return os.path.join('projects', 'images', instance.project.title, unique_filename)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name = "URL")    
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Date created")
    time_update = models.DateTimeField(auto_now=True, verbose_name = "Date modified")
    git_url = models.URLField(blank=True, null=True, verbose_name="URL address (git, leetcode...)")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"project_slug": self.slug})
    
    class Meta:
        verbose_name = 'Project'

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_upload_to)

    def __str__(self):
        return f"{self.project.title} Image"
    
    class Meta: 
        verbose_name = 'Images (for Project)'
        verbose_name_plural = 'Images (for Project)'






