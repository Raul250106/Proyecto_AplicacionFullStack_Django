from django.contrib import admin
from .models import Movie
from .models import Director
# Register your models here.
@admin.register(Movie, Director)
class MoviesAdmin(admin.ModelAdmin):
    pass
