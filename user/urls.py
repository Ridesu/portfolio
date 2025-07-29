from django.urls import path

from user.views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout1, name='logout'),
    path('changepass/', ChangePassword.as_view(), name="change")
]