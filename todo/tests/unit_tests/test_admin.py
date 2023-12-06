from django.test import TestCase, Client
from django.contrib.auth.models import User
from todo.models import TodoItem, Tag
from django.test import TestCase, RequestFactory
from django.contrib.admin.sites import AdminSite
from todo.admin import TodoItemAdmin

class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='adminpass')
        self.client.force_login(self.user)
        self.factory = RequestFactory()
        self.admin_site = AdminSite()
        
    def test_todo_item_admin(self):
        # Create a TodoItem instance
        todo_item = TodoItem.objects.create(title='Test Todo', description='Test Description', status='pending')

        # Simulate accessing the TodoItem admin change page
        response = self.client.get(f'/admin/todo/todoitem/{todo_item.id}/change/',follow=True)
        self.assertEqual(response.status_code, 200)

        # Simulate saving a TodoItem and check for validation error on timestamp edit

    def test_tag_admin(self):
        # Create a Tag instance
        tag = Tag.objects.create(name='Test Tag')

        # Simulate accessing the Tag admin change page
        response = self.client.get(f'/admin/todo/tag/{tag.id}/change/')
        self.assertEqual(response.status_code, 200)
        
    def test_todo_item_admin_clean_method(self):
        # Test clean method with timestamp
        todo_item = TodoItem.objects.create(title='Test Todo', description='Test Description', status='pending', timestamp='2023-01-01')
        response = self.client.post(
            f'/admin/todo/todoitem/{todo_item.id}/change/',
            {
                'title': 'Updated Title',
                'description': 'Updated Description',
                'due_date': '2023-12-31',
                'status': 'completed',
                'timestamp': '2023-12-05 12:00:00',  # Attempting to edit the timestamp
            }
        )
        self.assertEqual(response.status_code,200)

    def test_todo_item_admin_clean_method_no_timestamp(self):
        # Test clean method without timestamp
        todo_item = TodoItem.objects.create(title='Test Todo', description='Test Description', status='pending')
        response = self.client.post(
            f'/admin/todo/todoitem/{todo_item.id}/change/',
            {
                'title': 'Updated Title',
                'description': 'Updated Description',
                'due_date': '2023-12-31',
                'status': 'completed',
            }
        )
        self.assertEqual(response.status_code, 200)  

    def test_tag_admin_list_display(self):
        # Test list_display
        tag = Tag.objects.create(name='Test Tag')
        response = self.client.get('/admin/todo/tag/')
        self.assertContains(response, 'Test Tag')  # Check if tag name is displayed in the list view

    def test_tag_admin_add_tag(self):
        # Test adding a new tag through admin
        response = self.client.post('/admin/todo/tag/add/', {'name': 'New Tag'})
        self.assertEqual(response.status_code, 302)  # Check if successfully added
        
        # Check if the newly added tag exists
        self.assertTrue(Tag.objects.filter(name='New Tag').exists())
        