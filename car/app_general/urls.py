from django.urls import path, include
from app_general import views

urlpatterns = [
    path("",views.index,name='index'),
]