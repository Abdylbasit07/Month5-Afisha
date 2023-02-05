from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='No description!')
    duration = models.FloatField(default=0.00)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)



class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

