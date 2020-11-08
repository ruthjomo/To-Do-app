from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt

# # Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    tasks = TaskList.objects.all() 
    categories = Category.objects.all() 
    
    if request.method == "POST": 
        if "updateTask" in request.POST: 
            title = request.POST["description"]
            date = str(request.POST["date"]) 
            category = request.POST["category_select"] 
            content = title + " -- " + date + " " + category 
            task = TaskList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            task.save()  
            return redirect("/") 
        if "deleteTask" in request.POST: 
            checkedlist = request.POST["checkedbox"] 
            for task_id in checkedlist:
                task = TaskList.objects.get(id=int(task_id)) 
                task.delete() 
    return render(request, "index.html", {"tasks": tasks, "categories":categories})




@login_required(login_url='/accounts/login/')
def profile(request):
    tasks = TaskList.objects.all()
    return render(request,'profile.html' ,{'tasks':tasks})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    update_user=UpdateUser(request.POST,instance=request.user)
    update_profile=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if update_user.is_valid() and update_profile.is_valid():
        update_user.save()
        update_profile.save()
        
        messages.success(request, 'Profile Updated Successfully')
        return redirect('profile')
    
    else:
        update_user=UpdateUser(instance=request.user)
        update_profile=UpdateProfile(instance=request.user.profile)
    return render(request, 'update_profile.html',{'update_user':update_user,'update_profile':update_profile})


@login_required(login_url='/accounts/login/')
def updateTask(request,pk):
    task = TaskList.objects.get(id=pk)
    
    form = TaskForm(instance=task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

    return redirect('index')
        

    context = {'form':form}
    return render(request, 'update_task.html',context)

@login_required(login_url='/accounts/login/')
def deleteTask(request,pk):
    tasks = TaskList.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('index')

    context = {'tasks':tasks}
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




