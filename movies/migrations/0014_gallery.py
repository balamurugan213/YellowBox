# Generated by Django 3.0.7 on 2020-10-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_movie_trailer_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_slug', models.SlugField()),
                ('gallery_img', models.ImageField(blank=True, default='default3.jpeg', upload_to='')),
            ],
        ),
    ]
