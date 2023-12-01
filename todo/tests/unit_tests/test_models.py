from django.test import TestCase
from todo.models import TodoItem

class TodoItemModelTest(TestCase):
    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.create(
            title='Test Item',
            description='Test Description',
            status='OPEN'
        )
        self.assertEqual(todo_item.title, 'Test Item')
        self.assertEqual(todo_item.description, 'Test Description')
        self.assertEqual(todo_item.status, 'OPEN')

    def test_str_representation(self):
        todo_item = TodoItem.objects.create(title='Test')
        self.assertEqual(str(todo_item), todo_item.title)
