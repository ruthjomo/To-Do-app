from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# # Create your models here.

class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) 
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name 
    

class TaskList(models.Model): 
#     task =models.CharField(max_length=250)
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    category = models.ForeignKey(Category, default="general") 
    class Meta:
        ordering = ["-created"] 
    def __str__(self):
        return self.title #name to be shown when called


class Profile(models.Model):
        contact = models.TextField
        email = models.EmailField(max_length=70, blank=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
        bio=models.TextField(blank=True)
        '''
        this is added to ensure the linter has no errors saying class has no objects member in VS Code IDE
        '''
        objects = models.Manager()

        def save_profile(self):
            self.save()
    
@classmethod
def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

@classmethod
def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

@classmethod
def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

@classmethod
def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

class Meta:
        ordering = ['user']

