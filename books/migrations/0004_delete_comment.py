# Generated by Django 4.2.7 on 2023-12-23 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_marked_book_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]