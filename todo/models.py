from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


# Defining tag table

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Use to customize the representation of the model


class TodoItem(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("WORKING", "Working"),
        ("DONE", "Done"),
        ("OVERDUE", "Overdue"),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Using ManyToManyField for tags
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    # Use to customize the representation of the model.
    def __str__(self):
        return self.title
    
    # allows you to perform custom validation beyond what can be achieved using field options like max_length, blank, or null.

    def clean(self):
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.") # validation logic for the due_date
 