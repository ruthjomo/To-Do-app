from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt

# # Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    tasks = myTask.objects.all()
    form = myTaskForm()
     

    if request.method =='POST':
        form = myTaskForm(request.POST)
        if form.is_valid():
            form.save()

    # return redirect('index')
    
    context = {'tasks':tasks}
    return render(request,'list.html',context)

@login_required(login_url='/accounts/login/')
def updatemyTask(request,pk):
    task = Task.objects.get(id=pk)
    
    form = myTaskForm(instance=task)

    if request.method =='POST':
        form = myTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

    # return redirect('index')
        

    context = {'form':form}
    return render(request, 'update_task.html',context)

@login_required(login_url='/accounts/login/')
def deleteTask(request,pk):
    item = Task.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        # return redirect('index')

    context = {'item':item}
    return render(request,'delete_task.html',context)
    
@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    task = Task.get_profile_task(profile.id)
    title = f'@{profile.username}'
    return render(request, 'profile.html', {'title': title, 'profile': profile, 'profile_info': profile_info, 'tasks': tasks})




@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
         form = NewProfileForm(request.POST, request.FILES)
         if form.is_valid():
             profile = form.save(commit=False)
             profile.user = current_user
             profile.save()
        #  return redirect('index')

    else:
         form = NewProfileForm()
         return render(request, 'new_profile.html', {"form": form})


# # @login_required(login_url='/accounts/login/')