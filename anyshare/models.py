from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta

from django.db import models

class Invite(models.Model):
    email = models.EmailField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class UniqueURL(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=1)
