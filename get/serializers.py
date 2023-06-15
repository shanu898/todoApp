from rest_framework import serializers
from .models import get_tasks

class getTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_tasks
        fields=('id','desc','cDate','completed')