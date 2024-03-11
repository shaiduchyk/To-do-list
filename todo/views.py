from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def index(request: HttpRequest) -> HttpResponse:
    # user = request.user
    #
    # all_tasks = Task.objects.filter(assignees=user)
    # completed_tasks = all_tasks.filter(is_completed=True)
    # incompleted_tasks = all_tasks.filter(is_completed=False)
    #
    # context = {
    #     "all_tasks": all_tasks.count(),
    #     "completed_tasks_count": completed_tasks.count(),
    #     "incompleted_tasks_count": incompleted_tasks.count(),
    # }
    #
    # return render(request, "todo/index.html", context)
    pass
