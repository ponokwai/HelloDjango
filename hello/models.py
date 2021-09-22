from django.db import models
from django.utils import timezone


class LogMessage(models.Model):
    first_name = models.CharField(max_length=500, null="true")
    last_name = models.CharField(max_length=500, null="true")
    age = models.SmallIntegerField(null="true")
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localdate(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
