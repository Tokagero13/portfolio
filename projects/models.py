from django.db import models

# Create your models here.
class MyCv(models.Model):
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
    image = models.ImageField(upload_to='projects/images/')

    def __str__(self):
        return self.title

class Repository(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='repositories')
    title = models.CharField(max_length=200)
    description = models.TextField()
    code = models.TextField()
    
    def __str__(self):
        return self.title