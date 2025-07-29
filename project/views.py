import os
from urllib.parse import unquote

from project.models import *
from project.static.project.forms import AddPostForm, ChangePost, ChangeProject, AddProjectForm

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

menu = [{'title': "Проєкти",'url_name': 'project'}, {'title': "Про автора", "url_name": 'about'}]

# Create your views here.
def index(request):
    p = SomeProject.objects.all()
    return render(request, 'main/main.html', {'post': p,'menu': menu, "title": "Головна сторінка програми", 'addurl': 'addpage'})

def view_project(request):
    p = ModelForProjects.objects.all()

    return render(request, 'projects/main.html', {'proj': p,'menu': menu, 'title': "Проєкти", 'addurl': 'addproject'})

def changePage(request, pk):
    if not request.user.is_authenticated:
            raise Http404

    if request.user.role != 'admin':
        raise Http404

    p = get_object_or_404(SomeProject, id=pk)

    if request.method == 'POST':
        form = ChangePost(request.POST, instance=p)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    else:
        form = ChangePost(instance=p)

    return render(request, 'control/control.html', {'form': form,'menu': menu, 'post': p, 'addurl': 'addpage'})

def add_project(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.user.role != 'admin':
        raise Http404

    if request.method == "POST":
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('project')
            except:
                form.add_error("<h1>Сталася помилка</h1>")
    else:
        form = AddProjectForm()

    return render(request, 'projects/create/create.html',{'form': form, 'menu': menu, 'title': "Створення проєкту", 'addurl': 'addproject'})


def changeProject(request, pk):
    if not request.user.is_authenticated:
            raise Http404

    if request.user.role != 'admin':
        raise Http404

    p = get_object_or_404(ModelForProjects, id=pk)

    if request.method == 'POST':
        form = ChangeProject(request.POST, instance=p)
        if(form.is_valid()):
            form.save()
            return redirect('project')
    else:
        form = ChangeProject(instance=p)

    returnUrl = "changeproject/" + str(pk) + "/"

    return render(request, 'control/control.html', {'form': form, 'post': p, 'addurl': 'addproject', 'returnUrl': returnUrl})

def add_page(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.user.role != 'admin':
        raise Http404

    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error("<h1>Сталася помилка</h1>")

    else:
        form = AddPostForm()

    return render(request, 'projects/create/create.html', {'form': form, 'menu': menu, 'title': "Створення проєкту", 'addurl': 'addpage'})

def del_page(request, pk):
    if not request.user.is_authenticated:
        raise Http404

    if request.user.role != 'admin':
        raise Http404

    some = SomeProject.objects.get(pk=pk)
    if some.image:
        some.image.delete()
    # Видалення об'єкта
    some.delete()

    return render(request, 'projects/delete/succses.html', {'menu': menu, 'addurl': 'addpage'})

def del_project(request, pk):
    if not request.user.is_authenticated:
        raise Http404

    if request.user.role != 'admin':
        raise Http404

    some = ModelForProjects.objects.get(pk=pk)

    # Видалення об'єкта
    some.delete()

    return render(request, 'projects/delete/succses.html', {'menu': menu, 'addurl': 'addpage'})

def see_page(request, pk):
    some = SomeProject.objects.get(pk=pk)

    return render(request, 'see/see.html', {'menu': menu, 'p': some, 'addurl': 'addpage'})

def about(request):
    return render(request, 'about/about.html', {'menu': menu, 'addurl': 'addpage'})