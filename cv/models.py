import re
from django.db import models
from django.core.validators import RegexValidator
from django.forms import ValidationError

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('Phone number must contain only numeric digits.')

def validate_name_format(value):
    pattern = r'^[A-Za-z\s]*$'
    if not re.match(pattern, value):
        raise ValidationError('Name must contain only letters and spaces.')

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First name", validators=[validate_name_format])
    last_name = models.CharField(max_length=50, verbose_name="Last name", validators=[validate_name_format])
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[validate_phone_number])
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Messages(models.Model):
    user = models.ForeignKey('PersonalInfo', related_name='messages', on_delete=models.CASCADE, verbose_name='messages')
    contact_us_msg = models.TextField(max_length=250, verbose_name='Message')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Time created')
    
    def __str__(self):
        return f"{self.time_created} message from {self.user.first_name}: \n{self.contact_us_msg}"

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
