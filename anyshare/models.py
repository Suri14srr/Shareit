from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta

class UniqueURL(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=1)
