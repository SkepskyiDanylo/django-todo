from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["is_done", "-created_at"]

    @property
    def deadline_passed(self):
        if self.deadline is None:
            return False
        return self.deadline < timezone.now()

    @property
    def deadline_display(self):
        if self.deadline is None:
            return
        return self.deadline.strftime("%m/%d/%Y, %H:%M:%S")

    def __str__(self):
        return f"Task: {self.pk}"