from django.contrib import admin
from .models import TodoItem
from django.core.exceptions import ValidationError  # Import ValidationError

class TodoItemAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)  # Make timestamp field readonly

    # Validation checks and fieldsets example
    def clean(self, request, obj=None):
        if obj is not None and obj.timestamp is not None:
            # Prevent changing timestamp
            raise ValidationError("You cannot edit the timestamp.")
        return super().clean(request, obj)

    fieldsets = (
        ('Details', {
            'fields': ('title', 'description', 'due_date', 'status')
        }),
        ('Tags', {
            'fields': ('tags',)
        })
    )

class TagAdmin(admin.ModelAdmin):
    # Define fieldsets if needed for Tag model
    pass

admin.site.register(TodoItem, TodoItemAdmin)
# admin.site.register(Tag, TagAdmin)
