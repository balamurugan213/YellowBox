# Generated by Django 3.0.7 on 2020-10-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_movie_posterimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_slug', models.SlugField()),
                ('review_title', models.CharField(blank=True, max_length=300)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='color',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('1', 'G'), ('2', 'PG-13'), ('3', 'R'), ('4', 'PG'), ('5', 'TV-MA')], max_length=1),
        ),
    ]