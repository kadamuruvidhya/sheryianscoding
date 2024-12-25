from django.urls import path
from .views import *

app_name='codingapp'

urlpatterns = [
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('callback/',callback,name='callback'),
    path('signin/',signin,name='signin'),
]