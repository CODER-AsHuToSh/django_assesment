from django.test import TestCase
from todo.models import TodoItem
from todo.api.serializers import TodoItemSerializer


class TodoItemSerializerTest(TestCase):
    def test_todo_item_serializer(self):
        todo_item = TodoItem.objects.create(
            title="Test Item", description="Test Description", status="OPEN"
        )
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(serializer.data["title"], "Test Item")
        self.assertEqual(serializer.data["description"], "Test Description")
        self.assertEqual(serializer.data["status"], "OPEN")
