from django.contrib import admin
from .models import task

# Register your models here.
@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display=['user','title','description','complete','create','task_priority','due_date','status']

