# Generated by Django 4.2.7 on 2023-12-25 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_rename_created_at_message_created_at_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_at_time',
            new_name='created_at',
        ),
    ]