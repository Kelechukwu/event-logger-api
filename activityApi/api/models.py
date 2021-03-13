import uuid

from django.db import models


class Event(models.Model):
    id = models.UUIDField(unique=True, editable=False,
                          default=uuid.uuid4, primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=False)
    environment = models.CharField(max_length=100, blank=False)
    component = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=1000, blank=False)
    data = models.JSONField()

    def __str__(self):
        return f'{self.email}: {self.message}'
