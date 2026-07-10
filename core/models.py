from django.db import models
from cloudinary.models import CloudinaryField

class Resume(models.Model):
    link = models.URLField()

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):

    thumbnail = CloudinaryField()
    title = models.CharField(max_length=225)
    description = models.TextField()
    order_number = models.IntegerField(default=1)
    technologies = models.ManyToManyField(Technology)
    is_active = models.BooleanField(default=True)
    github = models.URLField(null=True, blank=True)
    live_demo = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Recognition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=50)
    thumbnail = CloudinaryField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title