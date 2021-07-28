# Generated by Django 3.0.5 on 2021-07-12 12:25

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='Tag',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='PhotoTags',
        ),
    ]