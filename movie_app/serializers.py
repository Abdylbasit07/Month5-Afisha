from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = 'name '.split()

class DirectorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # director = DirectorSerializer()

    class Meta:
         model = Movie
         fields = 'title'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title director duration description'.split()


class ReviewSerializer(serializers.ModelSerializer):
    # movie = MovieSerializer()

    class Meta:
        model = Review
        fields = 'id text'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = '__all__'