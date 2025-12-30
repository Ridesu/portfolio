from django.urls import path

from project.views import *

urlpatterns = [
    path("", about, name='about'),
    path("addpage/", add_page, name='addpage'),
    path('deletepage/<int:pk>/', del_page, name='delpage'),
    path('changepage/<int:pk>/', changePage, name='change'),
    path('projects/', view_project, name='project'),
    path('changeproject/<int:pk>/', changeProject, name='changeProject'),
    path("addproject/", add_project, name='addproject'),
    path('deleteproject/<int:pk>/', del_project, name='delproject'),
    path('seepage/<int:pk>/', see_page, name='see'),
    path('blog', index, name='home'),
]