from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import getTasksSerializer
from .models import get_tasks

# Create your views here.

class get(viewsets.ModelViewSet):
    serializer_class=getTasksSerializer
    queryset=get_tasks.objects.all()