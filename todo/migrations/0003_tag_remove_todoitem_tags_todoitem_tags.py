# Generated by Django 4.2.7 on 2023-12-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todoitem_tags_delete_tag_todoitem_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='tags',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='todo.tag'),
        ),
    ]
