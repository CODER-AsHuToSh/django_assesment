from django.contrib import admin
from .models import TodoItem, Tag
from django.core.exceptions import ValidationError

class TodoItemAdmin(admin.ModelAdmin):
    readonly_fields = ("timestamp",)
    list_display = ("title", "due_date", "status")
    list_filter = ("status", "due_date")  # Add filters for status and due_date

    def clean(self, request, obj=None):
        if obj is not None and obj.timestamp is not None:
            raise ValidationError("You cannot edit the timestamp.")
        return super().clean(request, obj)

    fieldsets = (
        ("Details", {
            "fields": ("title", "description", "due_date", "status")
        }),
        ("Tags", {
            "fields": ("tags",)
        }),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Display tag names in the admin list view


admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Tag, TagAdmin)
