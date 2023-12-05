def test_create_todo_item_with_tags(self):
    data = {
        "title": "New Todo Item",
        "description": "Description for the new todo",
        "status": "WORKING",
        "due_date": "2023-12-31",
        "tags": [
            {"name": "TagG22AAQW2dd2"},
            {"name": "TagG23AA1W1dd22"}
        ]
    }
    response = self.client.post(reverse("todo-create"), data, format='json')
    self.assertEqual(response.status_code, 201)