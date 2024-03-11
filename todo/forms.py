from django import forms
from django.forms import DateInput

from todo.models import Task, Tags


class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags",
        ]

        widgets = {
            "deadline": DateInput(attrs={"type": "date"}),
        }


class TagsCreationForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ["name"]