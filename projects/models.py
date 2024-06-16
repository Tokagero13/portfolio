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

# Create your models here.
class CV(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/images/')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_upload_to)

    def __str__(self):
        return f"{self.project.title} Image"
