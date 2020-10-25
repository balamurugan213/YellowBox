from django.db import models

# Create your models here.


class Movie(models.Model):
    RATINGS = (
        ('1', 'G'),
        ('2', 'PG-13'),
        ('3', 'R'),
        ('4', 'PG'),
        ('5', 'TV-MA'),
        ('6', 'Not Rated'),
    )
    movie_title = models.CharField(max_length=100, blank=True)
    movie_subtitle = models.CharField(
        max_length=300, blank=True)
    director = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    rating = models.CharField(max_length=1, choices=RATINGS)
    runtime = models.IntegerField()
    summary = models.TextField()
    watch_now_netflix = models.BooleanField(blank=True, default=False)
    watch_now_amazon = models.BooleanField(blank=True, default=False)
    watch_now_youtube = models.BooleanField(blank=True, default=False)
    watch_now_netflix_link = models.CharField(max_length=300, blank=True)
    watch_now_amazon_link = models.CharField(max_length=300, blank=True)
    watch_now_youtube_link = models.CharField(max_length=300, blank=True)
    imdb = models.FloatField(blank=True, default=10.0)
    rotten = models.IntegerField(blank=True, default=100)
    thumbimg = models.ImageField(default='default.jpeg', blank=True)
    posterimg = models.ImageField(default='default3.jpeg', blank=True)
    movie_slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    color = models.IntegerField(default=1)
    trailer_link = models.CharField(max_length=500, blank=True)
    #
    #

    def __str__(self):
        return self.movie_title

    def snippet(self):
        return self.summary[:100]+'...'

class Review(models.Model):
    review_slug = models.SlugField()
    review_title = models.CharField(max_length=300, blank=True)
    summary = models.TextField()


    def __str__(self):
        return self.review_slug


class Gallery(models.Model):
    gallery_slug = models.SlugField()
    gallery_img = models.ImageField(default='default3.jpeg', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return self.gallery_slug