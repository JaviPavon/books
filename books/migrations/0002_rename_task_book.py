# Generated by Django 3.2.22 on 2023-11-16 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Book',
        ),
    ]
