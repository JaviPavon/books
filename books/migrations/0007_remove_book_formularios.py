# Generated by Django 4.2.7 on 2023-11-21 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_formularios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='formularios',
        ),
    ]
