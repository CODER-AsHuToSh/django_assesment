from rest_framework.test import APITestCase
from todo.models import TodoItem, Tag
from todo.api.serializers import TagSerializer, TodoItemSerializer

class TodoItemSerializerTest(APITestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')

    def test_create_todo_item_with_tags(self):
        # Create test data
        tag_data = [{'name': 'tag1'}, {'name': 'tag2'}]
        todo_data = {
            'title': 'Test Todo Item',
            'description': 'Test Description',
            'tags': tag_data
        }

        # Serialize and validate data
        serializer = TodoItemSerializer(data=todo_data)
        self.assertTrue(serializer.is_valid())

        # Call create method and check for successful creation
        todo_item = serializer.save()
        self.assertIsInstance(todo_item, TodoItem)
        self.assertEqual(todo_item.title, 'Test Todo Item')

        # Check tags are associated properly
        self.assertEqual(todo_item.tags.count(), 2)

    def test_create_todo_item_with_existing_tags(self):
        # Create test data with existing tags
        tag_data = [{'name': 'tag1'}, {'name': 'tag2'}]
        todo_data = {
            'title': 'Todo with existing tags',
            'description': 'Description with existing tags',
            'tags': tag_data
        }

        # Serialize and validate data
        serializer = TodoItemSerializer(data=todo_data)
        self.assertTrue(serializer.is_valid())

        # Call create method and check for successful creation
        todo_item = serializer.save()
        self.assertIsInstance(todo_item, TodoItem)
        self.assertEqual(todo_item.title, 'Todo with existing tags')

        # Check tags are associated properly
        self.assertEqual(todo_item.tags.count(), 2)

