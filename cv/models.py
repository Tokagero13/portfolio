from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First name")
    last_name = models.CharField(max_length=50, verbose_name="Last name")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Education(models.Model):
    cv = models.ForeignKey('CV', related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, verbose_name="Field of study")
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    cv = models.ForeignKey('CV', related_name='experience', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, verbose_name="Job title")
    company = models.CharField(max_length=200)
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Skill(models.Model):
    cv = models.ForeignKey('CV', related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name

class CVProject(models.Model):
    cv = models.ForeignKey('CV', related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cv_projects/images/', blank=True, null=True)

    def __str__(self):
        return self.title

class CV(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    summary = models.TextField()

    def __str__(self):
        return f"CV of {self.personal_info.first_name} {self.personal_info.last_name}"
