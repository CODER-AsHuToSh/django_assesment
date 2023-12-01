from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Other URLs of your project can go here if needed
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),  # Include the URLs from the 'todo' app
]
