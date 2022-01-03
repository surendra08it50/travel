from django.urls import path
from . import views

urlpatterns = [
    path("", views.cal, name ="cal"),
    path("addkaro", views.add, name ="ad")
]