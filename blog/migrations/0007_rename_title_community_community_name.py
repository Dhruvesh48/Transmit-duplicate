# Generated by Django 4.2.15 on 2024-09-03 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_remove_community_url_post_community"),
    ]

    operations = [
        migrations.RenameField(
            model_name="community",
            old_name="title",
            new_name="community_name",
        ),
    ]
