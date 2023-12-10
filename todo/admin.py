from django.contrib import admin
from .models import TodoItem, Tag
from django.core.exceptions import ValidationError

# (readonly_fields) --> Makes the timestamp field of the TodoItem model read-only in the admin interface, preventing users from editing it.

# fieldsets --> Organizes the fields of the TodoItem model into different sections in the admin interface. It separates the fields into "Details" and "Tags" sections, defining how they are displayed and grouped together.

class TodoItemAdmin(admin.ModelAdmin):
    readonly_fields = ("timestamp",) 
    list_display = ("title", "due_date", "status")
    list_filter = ("status", "due_date")  # Add filters for status and due_date

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
