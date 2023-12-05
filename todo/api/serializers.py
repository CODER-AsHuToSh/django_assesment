from rest_framework import serializers
from todo.models import TodoItem, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = TodoItem
        fields = "__all__"

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')  # Remove tags from validated data
        todo_item = TodoItem.objects.create(**validated_data)  # Create TodoItem instance

        # Keep track of unique tags by name
        unique_tags = {}
        for tag_data in tags_data:
            tag_name = tag_data['name']
            if tag_name not in unique_tags:
                unique_tags[tag_name] = tag_data

        # Create tags and associate them with the created TodoItem
        for tag_data in unique_tags.values():
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            todo_item.tags.add(tag)

        return todo_item
