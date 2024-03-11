from django.contrib import admin

from todo.models import Task, Tags

admin.site.register(Tags)
admin.site.register(Task)
