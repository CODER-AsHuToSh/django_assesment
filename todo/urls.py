from django.urls import path
from .api.views import (
    TodoItemCreateView,
    TodoItemReadView,
    TodoItemListAllView,
    TodoItemUpdateView,
    TodoItemDeleteView,
    Home
)

urlpatterns = [
    path('', Home,name='home-page'),
    path('create/', TodoItemCreateView.as_view(), name='todo-create'),
    path('<int:pk>/', TodoItemReadView.as_view(), name='todo-read'),
    path('all/', TodoItemListAllView.as_view(), name='todo-list-all'),
    path('update/<int:pk>/', TodoItemUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoItemDeleteView.as_view(), name='todo-delete'),
]
