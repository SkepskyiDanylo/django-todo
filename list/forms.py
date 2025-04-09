from django import forms

from list.models import Tag, Task


class TagForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label="Name",
    )

    class Meta:
        model = Tag
        fields = ("name",)


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        label="Content",
        widget=forms.Textarea,
    )
    deadline = forms.DateTimeField(
        required=False,
        label="Deadline",
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Tags:",
    )
    is_done = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput,
        label="Completed",
    )
    class Meta:
        model = Task
        fields = ("content", "deadline", "is_done", "tags")