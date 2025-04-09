from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from list.forms import TagForm, TaskForm
from list.models import Tag, Task


class TagListView(ListView):
    model = Tag
    paginate_by = 5
    template_name = "list/tag-list.html"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "list/tag-form.html"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "list/tag-form.html"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")
    template_name = "list/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Tag"
        return context


class TaskList(ListView):
    queryset = Task.objects.all().prefetch_related("tags")
    model = Task
    paginate_by = 5
    template_name = "list/task-list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "list/task-form.html"
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "list/task-form.html"
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")
    template_name = "list/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Task"
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = "list/task-detail.html"