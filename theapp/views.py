from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# import datetime as dt
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.shortcuts import render, redirect

# # Create your views here.
def home(request):
    tasks = myTask.objects.all()
    form = myTaskForm()
     

    if request.method =='POST':
        form = myTaskForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/')
    
    context = {'tasks':tasks}
    return render(request,'list.html',context)
#     
# @login_required(login_url='/accounts/login/')
# def user_profile(request, username):
#     profile = User.objects.get(username=username)
#     try:
#         profile_info = Profile.get_profile(profile.id)
#     except:
#         profile_info = Profile.filter_by_id(profile.id)
#     businesses = Business.get_profile_businesses(profile.id)
#     title = f'@{profile.username}'
#     return render(request, 'profile.html', {'title': title, 'profile': profile, 'profile_info': profile_info, 'businesses': businesses})




# @login_required(login_url='/accounts/login/')
# def add_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#         return redirect('home')

#     else:
#         form = NewProfileForm()
#     return render(request, 'new_profile.html', {"form": form})


# # @login_required(login_url='/accounts/login/')