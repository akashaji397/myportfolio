from django.db import models
from django.contrib.auth.models import User

# About
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = 'About Me'

    def __str__(self):
        return "About Me"


from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a foreign key to User
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    course = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    job_company=models.CharField(max_length=50)
    year=models.IntegerField()
    job_role=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.job_company
    

# Recent Project Work
class RecentWork(models.Model):
    project_title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='works')
    project_description = models.TextField()

    def __str__(self):
        return self.project_title


class CV(models.Model):
    cv=models.FileField()