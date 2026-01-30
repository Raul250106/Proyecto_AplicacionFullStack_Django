from django.db import models

# Create your models here.
class Director (models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    age = models.IntegerField()
    birth = models.DateField()
    biography = models.TextField()
    picture = models.ImageField(upload_to='director_pictures/', null=True, blank=True, )

    def __str__(self):
        return self.name

class Movie (models.Model):
    title = models.CharField(max_length=25)
    genre = models.CharField(max_length=25)
    duration = models.IntegerField()
    year = models.IntegerField()
    synopsis = models.TextField()
    picture = models.ImageField(upload_to='movie_pictures/', null=True, blank=True)
    director = models.ForeignKey(Director, on_delete= models.SET_NULL, null= True, related_name="movies")

    def __str__(self):
        return self.title
    
