from datetime import datetime
import os

from django.db import models
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.forms import ValidationError
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
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    
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

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Education(models.Model):
    cv = models.ForeignKey('CV', related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    cv = models.ForeignKey('CV', related_name='experience', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Skill(models.Model):
    cv = models.ForeignKey('CV', related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name

class Project(models.Model):
    cv = models.ForeignKey('CV', related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)

    def __str__(self):
        return self.title

class CV(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    summary = models.TextField()

    def __str__(self):
        return f"CV of {self.personal_info.first_name} {self.personal_info.last_name}"

