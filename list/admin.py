from django.contrib import admin
from django.contrib.auth.models import Group

from list.models import Tag, Task

admin.site.unregister(Group)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("created_at", )
    search_fields = ("created_at",)
    list_filter = ("created_at", "deadline")