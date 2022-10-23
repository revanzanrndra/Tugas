import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from todolist.models import Task
from todolist.forms import TaskForm

# Create your views here.
@login_required(login_url='/todolist/login/')
@csrf_exempt
def show_todolist(request):
    data = Task.objects.filter(user=request.user)

    context = {
        'task':data,
        'username':request.user,
    }
    return render(request, 'todolist.html', context)

def create_task(request):
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todolist')

    return render(request, 'create_task.html', {'form':form})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# Tugas 6
def get_todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task_ajax(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = Task(title=title, description=description, user=request.user)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def update_task(request, id):
    if request.method == "POST":
        task = Task.objects.filter(pk=id, user=request.user).first()
        task.is_finished = not task.is_finished
        task.save()
        
        return HttpResponse(b"UPDATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_task(request, id):
    if request.method == "DELETE":
        task = Task.objects.filter(pk=id, user=request.user).first()
        task.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()