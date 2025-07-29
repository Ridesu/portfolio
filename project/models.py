from django.db import models
from django.urls import reverse


# Create your models here.
class SomeProject(models.Model):
    title = models.CharField(max_length=155, verbose_name='Назва')
    description = models.TextField(verbose_name="Опис")
    image = models.ImageField(upload_to="projects/", verbose_name="Фото", blank=True)

    def get_absolute_url(self):
        return reverse('delpage', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('change', kwargs={'pk': self.pk})
    def get_see_url(self):
        return reverse('see', kwargs={'pk': self.pk})

class ModelForProjects(models.Model):
    title = models.CharField(max_length=155, verbose_name='Ім\'я проекту')
    description = models.TextField(verbose_name="Опис")
    image = models.ImageField(upload_to="projects/image", verbose_name="Фото", blank=True)
    url = models.URLField(max_length=255)

    def get_absolute_url(self):
        return reverse('delproject', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('changeProject', kwargs={'pk': self.pk})

