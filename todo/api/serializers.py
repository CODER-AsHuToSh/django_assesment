from rest_framework import serializers
from rest_framework.exceptions import NotFound
from todo.models import TodoItem, Tag
from django.utils import timezone

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = TodoItem
        fields = "__all__"

    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

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
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        
        if tags_data is not None:
            tags_serializer = self.fields['tags']
            # Loop through each tag data
            for tag_data in tags_data:
                tag_name = tag_data.get('name')
                if tag_name:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)

        return super().update(instance, validated_data)
