from django.contrib import admin
from .models import Movie
from .models import Review
from .models import Gallery
# Register your models here.

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Gallery)