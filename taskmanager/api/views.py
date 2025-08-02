from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

#viewsets.ModelViewSet
#This is a powerful DRF class that gives you a full 
# set of CRUD API operations automatically:
class TaskViewSet(viewsets.ModelViewSet):
    #This tells the viewset:
    #“Fetch all tasks from the database.”
    queryset = Task.objects.all()

#This tells the viewset:
#👉 “Use this serializer to convert data to/from JSON.”
#So whenever a task is sent/received through the API, 
# TaskSerializer will handle the translation and validation.
    
    serializer_class = TaskSerializer

