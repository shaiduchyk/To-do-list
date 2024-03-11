from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone

from todo.forms import TaskCreationForm, TagsCreationForm
from todo.models import Task, Tags


@login_required()
def index(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()
    completed_tasks = all_tasks.filter(is_completed=True)
    incompleted_tasks = all_tasks.filter(is_completed=False)

    context = {
        "all_tasks_count": all_tasks.count(),
        "completed_tasks_count": completed_tasks.count(),
        "incompleted_tasks_count": incompleted_tasks.count(),
    }

    return render(request, "todo/index.html", context)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "create_task.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tags
    form_class = TagsCreationForm
    success_url = reverse_lazy("todo:tag-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tags
    context_object_name = "tag_list"
    template_name = "tags_list.html"


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("todo:tag-list")


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tags


@login_required
def mark_as_done(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.done_at = timezone.now()
    task.save()
    return HttpResponseRedirect(
        request.META.get(
            "HTTP_REFERER",
            reverse_lazy(viewname="todo:tasks"))
    )


@login_required
def undo_mark_as_done(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.done_at = None
    task.save()
    return HttpResponseRedirect(
        request.META.get(
            "HTTP_REFERER",
            reverse_lazy(viewname="todo:task-list"))
    )