from django.urls import path

from todo.views import index

app_name = "todo"

urlpatterns = [
    path("", index, name="index")
]