from django.db import models

from notifications.tasks import task_send_notification


# Create your models here.
class Notification(models.Model):
    message = models.TextField()

    def save(self, *arg, **kwargs):
        task_send_notification(self.message)

        super().save(*arg, **kwargs)
