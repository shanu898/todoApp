from django.contrib import admin
from .models import get_tasks

# Register your models here.
class getAdmin(admin.ModelAdmin):
    list_display=("desc","cDate","completed")
    
admin.site.register(get_tasks,getAdmin)
