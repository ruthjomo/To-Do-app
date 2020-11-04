from django.db import models
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# import datetime as dt

# # Create your models here.
class myTask(models.Model):
    title = models.CharField(max_length=200)
    complete= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#     contact = HTMLField()
#     email = models.EmailField(max_length=70, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
#     '''
#     this is added to ensure the linter has no errors saying class has no objects member in VS Code IDE
#     '''
#     objects = models.Manager()

#     def save_profile(self):
#         self.save()

#     @classmethod
#     def get_profile(cls, id):
#         profile = Profile.objects.get(user=id)
#         return profile

#     @classmethod
#     def get_all_profiles(cls):
#         profile = Profile.objects.all()
#         return profile

#     @classmethod
#     def find_profile(cls, search_term):
#         profile = Profile.objects.filter(user__username__icontains=search_term)
#         return profile

#     @classmethod
#     def filter_by_id(cls, id):
#         profile = Profile.objects.filter(user=id).first()
#         return profile

#     class Meta:
#         ordering = ['user']

