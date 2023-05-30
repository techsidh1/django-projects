from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Person(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=255)
    about_me = models.CharField(max_length=500)
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    tech_skills = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    github_link = models.CharField(max_length=255, null=True, blank=True)
    live_demo= models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title
    


class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='blogimages')    
    slug = models.SlugField(null=True, unique=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("mynotedetails", kwargs={"slug": self.slug})
    
    
 