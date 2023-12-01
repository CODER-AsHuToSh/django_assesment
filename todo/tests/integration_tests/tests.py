from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from todo.models import TodoItem
from todo.api.serializers import TodoItemSerializer


class TodoItemIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_item = TodoItem.objects.create(
            title="Test Item", description="Test Description", status="OPEN"
        )

    def test_home_page(self):
        response = self.client.get(reverse("home-page"))
        self.assertEqual(response.status_code, 200)

    def test_create_todo_item(self):
        data = {
            "title": "New Test Item",
            "description": "New Test Description",
            "status": "OPEN",
        }
        response = self.client.post(reverse("todo-create"), data)
        self.assertEqual(
            response.status_code, 201
        )  # Assuming successful creation returns 201

    def test_retrieve_todo_item(self):
        response = self.client.get(
            reverse("todo-read", kwargs={"pk": self.todo_item.pk})
        )
        self.assertEqual(response.status_code, 200)
        serialized_data = TodoItemSerializer(instance=self.todo_item).data
        self.assertEqual(response.data, serialized_data)

    def test_list_all_todo_items(self):
        response = self.client.get(reverse("todo-list-all"))
        self.assertEqual(response.status_code, 200)
        # Add assertions to check if all items are present in the response

    def test_update_todo_item(self):
        update_data = {
            "title": "Updated Test Item",
            "description": "Updated Test Description",
            "status": "DONE",
        }
        response = self.client.put(
            reverse("todo-update", kwargs={"pk": self.todo_item.pk}), update_data
        )
        self.assertEqual(response.status_code, 200)
        # Add assertions to check if the item was updated correctly

    def test_delete_todo_item(self):
        response = self.client.delete(
            reverse("todo-delete", kwargs={"pk": self.todo_item.pk})
        )
        self.assertEqual(
            response.status_code, 204
        )  # Assuming successful deletion returns 204
        # Add assertions to check if the item was deleted correctly
