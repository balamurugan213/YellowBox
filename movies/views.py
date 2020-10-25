from django.shortcuts import render
# from django.http import HttpResponse
from .models import Movie
from .models import Review
from .models import Gallery
# Create your views here.


# def about(request):
#     # return HttpResponse("about")
#     return render(request, 'about.html')


def movieHomepage(request):
    # return HttpResponse("homepage")
    movies = Movie.objects.all().order_by('date')
    return render(request, 'movies/movieList.html', {'movies': movies})


def movieDetailpage(request, slug):
    # return HttpResponse(slug)
    # articles = Article.objects.all().order_by('date')
    # return render(request, 'articles/articleHome.html', {'articles': articles})
    movie = Movie.objects.get(movie_slug=slug)
    review = Review.objects.filter(review_slug=slug).order_by('id')
    gallery = Gallery.objects.filter(gallery_slug=slug).order_by('id')
    return render(request, 'movies/movieDetailPage.html', {'movie': movie ,'reviews':review,'gallery':gallery})
