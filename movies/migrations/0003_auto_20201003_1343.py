# Generated by Django 3.0.7 on 2020-10-03 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201003_1335'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Movies',
        ),
    ]
