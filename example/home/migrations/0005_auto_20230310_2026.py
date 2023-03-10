# Generated by Django 4.1.7 on 2023-03-10 20:26

from django.db import migrations
from wagtail.blocks.migrations.migrate_operation import MigrateStreamData
from wagtail.blocks.migrations.operations import StreamChildrenToStructBlockOperation


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_homepage_body"),
    ]

    operations = [
        MigrateStreamData(
            app_name="home",
            model_name="HomePage",
            field_name="body",
            operations_and_block_paths=[
                (
                    StreamChildrenToStructBlockOperation("image", "extended_image"),
                    "",
                )
            ],
        ),
    ]
