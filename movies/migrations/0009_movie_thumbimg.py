# Generated by Django 3.0.7 on 2020-10-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20201003_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='thumbimg',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to=''),
        ),
    ]
