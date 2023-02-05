from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name


    @property
    def movies_count(self):
        count = self.director_movies.count()
        return count
        



class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='No description!')
    duration = models.FloatField(default=0.00)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='director_movies')
    

    @property
    def rating(self):
        count = self.movies_reviews.count()
        if count == 0: return 0
        total = 0
        for i in self.movies_reviews.all():
            total += i.stars
        return total / count

    
    def __str__(self):
        return self.title

CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=CHOICES, default=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movies_reviews')

