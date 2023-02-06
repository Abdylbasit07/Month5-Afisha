from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer, MovieReviewSerilizer
from .models import Director, Movie, Review


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Error'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director)
        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        name = request.data.get('name')
        director.name = name
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Error!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director_id = director_id
        
        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Error!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review.text = text
        review.stars = stars
        review.movie_id = movie_id
        
        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movies_reviews_view(request):
    movre = Movie.objects.all()
    serializer = MovieReviewSerilizer(movre, many=True)

    return Response(data=serializer.data)