from django.urls import path

from todo.views import (
    index,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)

app_name = "todo"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/",
         TaskListView.as_view(),
         name="task-list"),
    path("tasks/<int:pk>/,",
         TaskDetailView.as_view(),
         name="task-detail"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),
    path("task_create/",
         TaskCreateView.as_view(),
         name="task-create"),
]