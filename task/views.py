from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import task
from .forms import taskfrom,UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
# retrive according to specific user and search task
def home(request):
    if request.user.is_authenticated:
        lst=task.objects.filter(user=request.user)
        count_task=lst.filter(complete=False).count()
        tsearch=request.GET.get('search_area','')
        if tsearch:
            lst=task.objects.filter(title__icontains=tsearch,user=request.user)
        
        return render(request,'task/home.html',{'lst':lst,'count_task':count_task,})
    else:
        return HttpResponseRedirect('sig')
# Add Task
def Add_task(request):
    if request.method=='POST':
        fm=taskfrom(request.POST)
        if fm.is_valid():
            fm.instance.user=request.user
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm=taskfrom()
    return render(request,'task/addtask.html',{'fm':fm})
#list detail
def detail(request,id):
    lst=task.objects.get(pk=id)
    return render(request,'task/details.html',{'lst':lst})
#update
def update(request,id):
    if request.method=='POST':
        pi=task.objects.get(pk=id)
        fm=taskfrom(request.POST, instance=pi)
        if fm.is_valid():
            print('valid')
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi=task.objects.get(pk=id)
        fm=taskfrom(instance=pi)
    return render(request,'task/update.html',{'fm':fm})
#delete
def delete(request,id):
    pi=task.objects.get(pk=id)
    if request.method=='POST':
        pi.delete()
        return redirect('/')
    
    return render(request,'task/delete.html', {'pi':pi})
#signup
def signup(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/log/')
    else:
        fm=UserCreationForm()
    return render(request,'task/signup.html',{'fm':fm})
#login
def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                messages.warning(request,'Invalid username or password or both')
            
    else:
        fm=AuthenticationForm()

    return render(request,'task/login.html',{'fm':fm})
# logout
def user_logout( request):
    logout(request)
    return HttpResponseRedirect('/log/')
# changepassword without oldpassword
def change_pass(request):
    if request.method=='POST':
        fm=SetPasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.SUCCESS(request,'New password is set')
            return HttpResponseRedirect('/log/')
    else:
        fm=SetPasswordForm(user=request.user)
    return render (request,'task/setpass.html',{'fm':fm})



    

