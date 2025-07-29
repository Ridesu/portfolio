from django import forms

from project.models import SomeProject


class AddPostForm(forms.ModelForm):
    class Meta:
        model = SomeProject
        fields = ['title', 'description', 'image']