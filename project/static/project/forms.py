from django import forms

from project.models import SomeProject, ModelForProjects


class AddPostForm(forms.ModelForm):
    class Meta:
        model = SomeProject
        fields = ['title', 'description', 'image']

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = ModelForProjects
        fields = ['title', 'description', 'image', 'url']

class ChangePost(forms.ModelForm):
       class Meta:
           model = SomeProject
           fields = ['title', 'description']


class ChangeProject(forms.ModelForm):
    class Meta:
        model = ModelForProjects
        fields = ['title', 'description', 'image']