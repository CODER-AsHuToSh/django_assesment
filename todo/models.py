from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True)  # Using CharField to store comma-separated tags
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.tags:
            # Splitting the tags by comma, making them unique, and joining back
            unique_tags = list(set([tag.strip() for tag in self.tags.split(',')]))
            self.tags = ','.join(unique_tags)
        super().save(*args, **kwargs)
