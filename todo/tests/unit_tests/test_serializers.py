from django.test import TestCase
from todo.models import TodoItem, Tag
from todo.api.serializers import TagSerializer, TodoItemSerializer

class TagSerializerTest(TestCase):
    def test_tag_serializer(self):
        tag_data = {'name': 'Test Tag'}
        serializer = TagSerializer(data=tag_data)
        self.assertTrue(serializer.is_valid())
        tag_instance = serializer.save()
        self.assertIsInstance(tag_instance, Tag)
        self.assertEqual(tag_instance.name, 'Test Tag')

class TodoItemSerializerTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')

    def test_todo_item_serializer_create(self):
        todo_data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'tags': [{'name': 'Tag1'}, {'name': 'Tag2'}]
        }
        serializer = TodoItemSerializer(data=todo_data)
        self.assertTrue(serializer.is_valid())
        todo_instance = serializer.save()
        self.assertIsInstance(todo_instance, TodoItem)
        self.assertEqual(todo_instance.title, 'Test Todo')
        self.assertEqual(todo_instance.description, 'Test Description')
        self.assertEqual(todo_instance.tags.count(), 2)

    def test_todo_item_serializer_update(self):
        todo_item = TodoItem.objects.create(title='Existing Todo', description='Existing Description')
        todo_data = {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'tags': [{'name': 'Tag1'}, {'name': 'Tag3'}]  # 'Tag3' doesn't exist yet
        }
        serializer = TodoItemSerializer(instance=todo_item, data=todo_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_todo = serializer.save()
        self.assertEqual(updated_todo.title, 'Updated Todo')
        self.assertEqual(updated_todo.description, 'Updated Description')
        self.assertEqual(updated_todo.tags.count(), 2)  # One existing and one newly created tag
